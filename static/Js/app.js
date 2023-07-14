// Obtener habitaciones
axios.get('http://localhost:5000/habitaciones')
  .then(response => {
    const habitaciones = response.data;
    // Hacer algo con las habitaciones obtenidas
  })
  .catch(error => {
    console.error(error);
  });

// Crear una nueva habitación
const nuevaHabitacion = { nombre: 'Habitación 1', precio: 100 };
axios.post('http://localhost:5000/habitaciones', nuevaHabitacion)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });

  axios.get('habitaciones.json')
  .then(response => {
    const habitaciones = response.data;
    // Hacer algo con las habitaciones obtenidas
  })
  .catch(error => {
    console.error(error);
  });
