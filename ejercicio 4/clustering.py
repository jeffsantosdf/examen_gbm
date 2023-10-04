import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import os

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
df = pd.read_csv(dir + '/data_customer_classification.csv')

#Preparando los datos haciendo agregaciones
agg_clustering = df.groupby('customer_id').agg({'trans_date': 'count', 'tran_amount': ['mean', 'max']})
agg_clustering.columns = ['tran_count', 'avg_tran_amount', 'max_tran_amount']

def asignacion(tran):
    if tran['tran_count'] < 10 and tran['avg_tran_amount'] < 50 and tran['max_tran_amount'] < 100:
        return 'low'
    elif tran['tran_count'] >= 10 and tran['avg_tran_amount'] >= 50 and tran['max_tran_amount'] >= 100:
        return 'high'
    else:
        return 'medium'

agg_clustering['categoria'] = agg_clustering.apply(asignacion, axis=1)

#  Al tratarse de un problema de clasificación multiclase se debe utilizar One-Hot Encoding para 
# poder formatear la salida.
label_encoder = LabelEncoder()
agg_clustering['categoria_encoded'] = label_encoder.fit_transform(agg_clustering['categoria'])

X = agg_clustering[['tran_count', 'avg_tran_amount', 'max_tran_amount']].values
y = agg_clustering['categoria_encoded'].values

# Haciendo Split a los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Preprocesando los datos con la técnica de escalado de datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Construyendo modelo
model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compilando
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenando el modelo
model.fit(X_train, y_train, epochs=150, batch_size=10, validation_split=0.1, verbose=0)

# Evaluando el modelo
scores = model.evaluate(X_test, y_test, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

with open(dir + '/output.txt', 'w') as output:
    output.write("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100) + '\n')

# Realizar predicciones en los datos de prueba 
X_new = X_test[:20]
predicciones = model.predict(X_new)
y_predict = np.argmax(predicciones, axis=1)
transformacion = label_encoder.inverse_transform(y_predict)
y_test_original = label_encoder.inverse_transform(y_test)

with open(dir + '/output.txt', 'a') as output:
    for i in range(20):
        linea = '%s --> %s (resultado real %s)\n' % (X_new[i].tolist(), transformacion[i], y_test_original[i])
        output.write(linea)
