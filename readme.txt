Este proyecto toma un modelo preentrenado de YOLO que es una libreria para hacer deeplearning y video analitica.
El archivo create, crea una version inicial de un modelo que queda guardado en "yolov8n.pt".
Al ser una version inicial detecta objetos que no son necesarios, objetos como bolsos o carros, para evitar esto
se debe hacer un entrenamiento del model para cambiar su comportamiento y enseñarle que solo debe leer personas.

Segun lo leido se recomienda hacer el conteo o reconicimiento de personas enfocandose en las cabezas,
este video detalla a fondo lo mencionado anteriormente "https://www.youtube.com/watch?v=d1bky80NXeQ"
aqui se explica como y porque se debe hacer de esta forma.

El archivo retrain lee el modelo guardado anteriormente como "yolov8n.pt" la intension de este segundo archivo
es trabajar en la presicion del modelo y su comportamiento, ademas en dicho archivo se encuentra una linea de codigo
que se encarga de guardar el progreso del entrenamiento del modelo.