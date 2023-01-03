
function addToDb(){
    $('#myForm').submit(function(event) {
        event.preventDefault();
        let hand_name = $('#hand_name').val();
        let result = $('#status').val();
        $.post("http://127.0.0.1:5002/game/save", { hand_name: hand_name, status: result }, function(data) {
        // handle the response from the server-side script
        });
    });
}




// $(document).ready(function(){
//     $("button").click(function(){
//       $.post("demo_test_post.asp",
//       {
//         name: "Donald Duck",
//         city: "Duckburg"
//       },
//       function(data,status){
//         alert("Data: " + data + "\nStatus: " + status);
//       });
//     });
//   });

// $(".send__data__btn").click(function(){
//     $.post("http://localhost:5002/add_game_to_db",
//     {
//       hand_name: hand_name,
//       status: result
//     },
//     function(data, status){
//         alert("Data: " + data + "\nStatus: " + status);
//     });
//   });

// const btn = document.querySelector('.send__data__btn');

// btn.addEventListener('click', function () {

//     fetch('http://localhost:5002/add_game_to_db', {
//         headers : {
//             'Content-Type' : 'application/json'
//         },
//         method : 'POST',
//         body : JSON.stringify( {
//             'hand_name' : hand_name,
//             'status' : result
//         })
//     })
//     .then(function (response){

//         if(response.ok) {
//             response.json()
//             .then(function(response) {
//                 console.log(response);
//             });
//         }
//         else {
//             throw Error('Something went wrong');
//         }
//     })
//     .catch(function(error) {
//         console.log(error);
//     });
// });
