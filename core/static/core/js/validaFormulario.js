$(function () {
    $("#formulario_contacto").validate({
        rules:
        {
            rut:
            {
                minlength: 7,
                maxlength: 10,
                rut: true,
                required: true,
            },
            email:
            {
                email:true,
                required:true,
                minlength:6,
                maxlength:100,
            },
            confirmar_email:
            {
                required:true,
                equalTo:"#email",
            },
            password:
            {
                required:true,
                minlength:6,
                maxlength:15,
            },
            password_confirm:
            {
                required:true,
                equalTo:"#password",
            },
            fecha_reg:
            {
                required:true,
            },
            nombre:
            {
                required:true,
            },
            apellido:
            {
                required:true,
            },
            fecha_nac:
            {
                required:true,
            },
            pais:
            {
                required:true,
            },
            comentarios:
            {
                required:true,
                maxlength: 150,
            }
        },
        messages:
        {
            rut:
            {
                required: "Debes ingresar un rut",
                minlength: "Debes ingresar entre 7 y 10 caracteres",
                maxlength: "Debes ingresar entre 7 y 10 caracteres",
                rut: "Rut Inválido, ingréselo nuevamente",
            },
            email:
            {
                email:"Formato de email no válido.",
                required:"Debes ingresar un email válido",
                minlength:"Debes ingresar a lo menos 6 caracteres",
                maxlength:"Excedes el largo máximo permitido.",
            },
            confirmar_email:
            {
                email:"Formato de email no válido.",
                required:"Debes reingresar el correo",
                equalTo:"El correo ingresado no es igual al anterior",
            },
            password:
            {
                required:"Debes ingresar un password",
                minlength:"Debes ingresar entre 6 a 15 carateres.",
                maxlength:"Debes ingresar entre 6 a 15 carateres.",
            },
            password_confirm:
            {
                required:"Debes reingresar el password.",
                equalTo:"El password ingresado no es igual al anterior.",
            },
            fecha_reg:
            {
                required:"Debes ingresar una fecha válida.",
            },
            nombre:
            {
                required:"Debes ingresar un nombre."
            },
            apellido:
            {
                required:"Debes ingresar un apellido.",
            },
            
            fecha_nac:
            {
                required:"Debes ingresar la fecha de nacimiento.",
            },
            pais:
            {
                required:"Debes seleccionar el pais.",
            },
            comentarios:
            {
                required:"Debes ingresar un comentario.",
                maxlength: "Superas el máximo de 150 caracteres.",
            }
        }
    })
})

