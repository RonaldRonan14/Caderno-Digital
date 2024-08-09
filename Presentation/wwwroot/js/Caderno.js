function PreDelete(button){
    const anotacaoTitulo = button.getAttribute("data-anotacao-titulo");
    const inputId = document.getElementById("anotacao-id");
    const spanTitulo = document.getElementById("anotacao-titulo");

    spanTitulo.innerText = anotacaoTitulo;
    inputId.value = button.getAttribute("data-anotacao-id");
}