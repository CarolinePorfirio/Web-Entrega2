function validaRut(rutx) {
    // Despejar Puntos
    var valor = rutx.value.replace(/./g, '');
    // Despejar Guión
    valor = rutx.value.replace(/-/g, '');

    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0,-1);
    dv = valor.slice(-1).toUpperCase();
    
    // Formatear RUN
    rutx.value = cuerpo + '-'+ dv

    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if(cuerpo.length < 7) { return false; }
    
    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;
    
    // Para cada dígito del Cuerpo
    for(i=1;i<=cuerpo.length;i++) {
    
        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);
        
        // Sumar al Contador General
        suma = suma + index;
        
        // Consolidar Múltiplo dentro del rango [2,7]
        if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
  
    }
    
    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);
    
    // Casos Especiales (0 y K)
    dv = (dv == 'K')?10:dv;
    dv = (dv == 0)?11:dv;
    
    // Validar que el Cuerpo coincide con su Dígito Verificador
    if(dvEsperado != dv) {return false; }
    
    // Si todo sale bien, eliminar errores (decretar que es válido)
    rutx.setCustomValidity('salida limpia');
    return true;
}


function contar(valor) {
    resta = valor.value.length;
    total = 150-resta;
    document.getElementById("contador").innerHTML = total;
}

function cuentaerror(){
    var contval=0;
    
console.log("valor validacion rut "+document.getElementById("rut").formNoValidate)

    if (document.getElementById("rut").form.checkValidity()){contval +=1;}
    if (document.getElementById("pasaporte").form.checkValidity()){contval +=1;}
    if (document.getElementById("nombre").form.checkValidity()){contval +=1;}
    if (document.getElementById("apellido").form.checkValidity()){contval +=1;}
    if (document.getElementById("email").form.checkValidity()){contval +=1;}
    if (document.getElementById("fecha_nac").form.checkValidity()){contval +=1;}
    if (document.getElementById("pais").form.checkValidity()){contval +=1;}
    if (document.getElementById("comentarios").form.checkValidity()){contval +=1;}

    console.log("validacion contador "+ contval);
    return contval;
}

function confirmacion() {
    var valform = document.getElementById("rut");
    valform.checkValidity();
    console.log("tipo de objeto    " + document.querySelectorAll('.valid').value);

    var contvalf=cuentaerror();

    if (contvalf == 0  &&  document.querySelectorAll('.error').length == 0){
        console.log("formulario enviado");
           var Rut = document.getElementById("rut").value;
        var Pasaporte= document.getElementById("pasaporte").value;
        var Nombre = document.getElementById("nombre").value;
        var Apellido = document.getElementById("apellido").value;
        var Email = document.getElementById("email").value;
        var fhc_nac = document.getElementById("fecha_nac").value;
        var Pais = document.getElementById("pais").value;
        var Genero = '';
        if(document.querySelector('input[name="genero"]:checked')){
            Genero = document.querySelector('input[name="genero"]:checked').value;
        }
        var Interes = '';
        if( document.getElementById("interes1").checked == true){
            Interes = document.getElementById("interes1").value;
        }
        if( document.getElementById("interes2").checked == true){
            if(Interes.length > 0){Interes = Interes + " , "}
            Interes = Interes + document.getElementById("interes2").value;
        }
        if( document.getElementById("interes3").checked == true){
            if(Interes.length > 0){Interes = Interes + " , "}
            Interes = Interes + document.getElementById("interes3").value;
        }
        var Comentarios = document.getElementById("comentarios").value;

        alert("Datos ingresados:\n" +
        "Rut:".padEnd(24,' ') + Rut + "\n" +
        "Pasaporte:".padEnd(20,' ') + Pasaporte + "\n" +
        "Nombre:".padEnd(20,' ') + Nombre + "\n" +
        "Apellido:".padEnd(22,' ') + Apellido + "\n" +
        "Email:".padEnd(24,' ') + Email + "\n" +
        "Fch Nac:".padEnd(21,' ') + fhc_nac + "\n" +
        "Pais:".padEnd(24,' ') + Pais + "\n" +
        "Genero:".padEnd(21,' ') + Genero + "\n" +
        "Intereses:".padEnd(21,' ') + Interes + "\n" +
        "Comentarios:".padEnd(18,' ') + Comentarios);

        
    }
    
    }

    function CrearArreglo() {
        for (i = 0; i<CrearArreglo.arguments.length; i++)
        this[i + 1] = CrearArreglo.arguments[i];}
    
    function IniciaReloj(){
    
        var meses = new CrearArreglo('Enero','Febrero','Marzo','Abril','Mayo',
        'Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre');
        var fecha = new Date();
        var dia = fecha.getDate();
        var mes = fecha.getMonth() + 1;
        var yy = fecha.getYear();
        var anio = (yy < 1000) ? yy + 1900 : yy;
        //today=new Date();
        var hora=fecha.getHours();
        var min=fecha.getMinutes();
        var seg=fecha.getSeconds();
        min=ValidarH(min);
        seg=ValidarH(seg);
        document.getElementById('reloj').innerHTML=("Santiago.Chile " + dia + " de " + meses[mes] + " del " + anio +" : "+hora+":"+min+":"+seg);
        t=setTimeout('IniciaReloj()',500);}
    
    
    function ValidarH(i)
    {
        if (i<10) {
            i="0" + i;
        }
        return i;
    }
    
    window.onload=function()
    {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open ('GET','https://mindicador.cl/api',true);
        xmlHttp.send();
    
        var dolar = 0;
        var euro = 0;
    
        xmlHttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200)
            {
                var data = JSON.parse(this.responseText);
                uf = data.uf.valor;
                dolar = data.dolar.valor;
                euro = data.euro.valor;
            }
            document.getElementById("valord").innerHTML = dolar;
            document.getElementById("valore").innerHTML = euro;
        };
        IniciaReloj();
    }
    
    function CambioDivisa(){
       
        var valorconvertir =0;
        valorconvertir =document.getElementById('monto').value;
    
        //verificar seleccion
        var seleccion =   document.querySelector('input[name="divisa"]:checked').value;
     
        //si es dolar
        var montodivisa=1;
        if (seleccion == "DOLAR")
        {
            montodivisa=document.getElementById('valord').innerHTML;
        }
        
        //si es euro
        if (seleccion == "EURO")
        {
            montodivisa=document.getElementById('valore').innerHTML;

        }
    
        var total = valorconvertir * montodivisa
      
        //modifica lebel del monto
        document.getElementById('resultado').innerHTML=new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(total);
    }
    