function acaoBotao(){

var numero, fatorial, contador 
numero = prompt("Digite o número para calcular o fatorial.")
fatorial = 1
for (var contador = 1; contador <= numero; contador++) {
	fatorial = fatorial * contador
}
document.getElementById("botao").innerText = "O fatorial de " + numero + " é: " + fatorial
}  
