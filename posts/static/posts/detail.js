console.log('Hola details para poder datos');
const postBox = document.getElementById('post-box')
const backBtn = document.getElementById('back-btn')
const updateBtn = document.getElementById('update-btn')
const deleteBtn = document.getElementById('delete-btn')
const url = window.location.href + "data/"
const spinnerBox = document.getElementById('spinner-box')

// update
const titleInput = document.getElementById('id_title')
const bodyInput = document.getElementById('id_body')



backBtn.addEventListener('click', ()=>{
  history.back()
})

$.ajax({
  type: 'GET',
  url: url,
  success: function(response){
    console.log(response);
    const data = response.data

    if (data.logged_in !== data.author){
      console.log('diferrente');
    }else{
      console.log('the same');
      updateBtn.classList.remove('not-visible')
      deleteBtn.classList.remove('not-visible')
    }

    //Codigo para poder mostrar details.html
    const titleEl= document.createElement('h3')
    titleEl.setAttribute('class','mt-3')

    const bodyEl= document.createElement('p')
    bodyEl.setAttribute('class','mt-1')

    titleEl.textContent = data.title
    bodyEl.textContent = data.body


    postBox.appendChild(titleEl)
    postBox.appendChild(bodyEl)
    //----------//
    //Codigo para poder mostrar en modal de update
    titleInput.value = data.title
    bodyInput.value = data.body
    //---//


    spinnerBox.classList.add('not-visible')
  },
  error: function(error){
    console.log(error);
  }
})