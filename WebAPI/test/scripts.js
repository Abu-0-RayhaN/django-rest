//GET Request
// axios.get("http://localhost:8000/status/status/list/")
// .then(response => console.log(response))
//POST Request
// let status = {
//     user:1,
//     content : "I am testing data!",
//     image: null
// }
// axios.post("http://localhost:8000/status/status/create/",status,{
//     headers:{
//         "Content-Type": "application/json"
//     }
// })
// .then(response => console.log(response))
// .catch(erro=> console.log(error.message))

//DELETE Request
// axios.delete("")
// .then(response => console.log(respone))


//PUT Request
document.getElementById('myform').addEventListener('submit', handleSubmit);
document.getElementById('image').addEventListener('change',handleImage);

let myImage = null
function handleImage(){
    myImage= e.target.files[0];
    console.log(myImage);
}
function handleSubmit(){
    e.preventDefault();
    let user= document.getElementById('user').value;
    let content = document.getElementById('content').value;
    //content type =>
    let form_data = new FormData();
    form_data.append('user',user);
    form_data.append('content',content);
    form_data.append('image',myImage);

    for (var [key, value] of form_data.entries()){
        console.log(key, ":", value)
    }
}