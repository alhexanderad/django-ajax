console.log('Loremamdkfkasdfksadkfas,d');

const helloWorldBox = document.getElementById('hello-world');
const postsBox = document.getElementById('posts-box');
const spinnerBox = document.getElementById('spinner-border');

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

$.ajax({
  type:'GET',
  url:'data/',
  success:function(response){
    console.log('Informacion de Get data ajax');
    console.log(response)
    const data = response.data
    setTimeout(()=>{
      spinnerBox.classList.add('not-visible');
      console.log(data);
      data.forEach(el => {
        postsBox.innerHTML +=`
          ${el.title} - <b>${el.body}</b><br>
          `
      });
    }, 1000)
  },
  error: function(error){
    console.log(error);
  }
})