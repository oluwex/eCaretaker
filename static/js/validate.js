/**
 * Created by Habeeb.Oluwo on 26-Aug-16.
 */
function valid() {
$("#form").validate({
   rules:{
       username: "required",
       last_name: "required",
       first_name: "required",
       email: "required",
       password1: "required",
       password2: "required"
   },

   messages: {
       username: "Username field cannot be blank",
       last_name: "Username field cannot be blank",
       first_name: "Username field cannot be blank",
       email: "Username field cannot be blank",
       password: "Username field cannot be blank",
       password2: "Username field cannot be blank",
   }

});
}