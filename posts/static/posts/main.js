console.log('Hola Mundo estamos de vuelta 2022');

const helloWorldBox = document.getElementById('hello-world');



$.ajax({
  type: 'GET',
  url:' hello-world/',
  success: function(response){
    console.log('success',response.text)
    helloWorldBox.textContent = response.text
  },
  error: function(error){
    console.log('error', error);
  }
})