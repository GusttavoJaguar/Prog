//Bola de cristal (IDADE)
function acaoBotao() {
	
	var nome, ano_nasc, ano_atual, idade, limite, contador

	limite = prompt("Digite a quantidade de vezes que vai ser verificado a idade: ")
	contador = 0
	while(contador < limite){
		nome = prompt("Digite seu nome: ")
		musica = prompt("Cite algumas bandas, músicos ou tipos de músicas que mais gosta.")
		livro = prompt("Gosta de ler? Se sim, cite alguns que mais gostou de ler.")
		ano_nasc = prompt("Me diga, "  + nome + "! Em que ano você ,nasceu?")
		esporte = prompt("Gosta de esportes? Se sim, quais?")
		ano_atual = prompt("Em que ano você está fazendo esta consulta?")
		opiniao = prompt("O que acha do cenário que estamos vivendo, no contexto geral do nosso planeta?")
		idade = parseInt(ano_atual) - parseInt(ano_nasc)
		if (idade > 21)
			document.getElementById("botao").innerText = nome + " tem " + idade + " anos, já é uma pessoa adulta e vejo uma enorme determinação. Espero que esteja realizando todos os seus sonhos. Nunca desista."
		else
			document.getElementById("botao").innerText = nome + " tem " + idade + " anos, aproveite sua juventude com consciência. O futuro tem muitas portas te esperando para abrí-las. Nunca desista dos seus sonhos."
		contador++
	}
}

