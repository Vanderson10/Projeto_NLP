const tabs = document.querySelectorAll(".tab");

function showTab(tabId) {
  tabs.forEach((tab) => {
    tab.style.display = "none";
  });

  document.getElementById(tabId).style.display = "block";
}

// Função para atualizar o spinner com base na pontuação
function updateSpinnerWithScore(score) {
  const notaFinal = document.getElementById("notaFinal");
  const spinner = document.createElement("div");
  spinner.className = "spinner";
  const fill = document.createElement("div");
  fill.className = "fill";
  fill.style.width = (score / 1000) * 100 + "%";
  spinner.appendChild(fill);
  notaFinal.innerHTML = "";
  notaFinal.appendChild(spinner);
}

// Simule a obtenção da pontuação do backend (substitua pela pontuação real)
const feedback = {
  notaFinal: 750, // Substitua pela pontuação real (0 a 1000)
};

// Atualizar o spinner com a pontuação obtida
updateSpinnerWithScore(feedback.notaFinal);

function enviarRedacao() {
  // Criar div para centralizar o GIF e o texto
  const loadingDiv = document.createElement("div");
  loadingDiv.style.textAlign = "center";
  document.body.appendChild(loadingDiv);

  // Exibir o GIF e o texto
  const gif = document.createElement("img");
  gif.src = "https://usagif.com/wp-content/uploads/cat-typing-12.gif";
  gif.style.width = "200px"; // Ajuste o tamanho conforme necessário
  loadingDiv.appendChild(gif);

  const corrigindoText = document.createElement("p");
  corrigindoText.innerText = "Corrigindo...";
  corrigindoText.style.fontSize = "18px";
  loadingDiv.appendChild(corrigindoText);

  setTimeout(() => {
    // Remover o GIF e o texto após 5 segundos
    loadingDiv.parentNode.removeChild(loadingDiv);

    // Simule o envio da redação e recebimento do feedback do backend (substitua por chamadas reais ao backend)
    const feedback = {
      competencia1: 8.5,
      competencia2: 7.0,
      competencia3: 6.5,
      competencia4: 9.0,
      competencia5: 7.5,
      notaFinal: 38.5,
      errosGramaticais: ["Erro 1", "Erro 2"],
      comentariosGerais: "Bom trabalho, mas pode melhorar.",
      orientacoesReescrita: "Revise a estrutura do parágrafo de introdução.",
      linhaArgumentativa: "A linha argumentativa é clara e bem desenvolvida.",
      agentesApontados: "Você identificou os agentes históricos corretamente.",
    };

    // Atualizar os elementos na aba "Feedback" com os dados do feedback
    document.getElementById("competencia1").innerText = feedback.competencia1;
    document.getElementById("competencia2").innerText = feedback.competencia2;
    document.getElementById("competencia3").innerText = feedback.competencia3;
    document.getElementById("competencia4").innerText = feedback.competencia4;
    document.getElementById("competencia5").innerText = feedback.competencia5;
    document.getElementById("notaFinal").innerText = feedback.notaFinal;
    document.getElementById("errosGramaticais").innerText =
      feedback.errosGramaticais.join(", ");
    document.getElementById("comentariosGerais").innerText =
      feedback.comentariosGerais;
    document.getElementById("orientacoesReescrita").innerText =
      feedback.orientacoesReescrita;
    document.getElementById("linhaArgumentativa").innerText =
      feedback.linhaArgumentativa;
    document.getElementById("agentesApontados").innerText =
      feedback.agentesApontados;

    // Mudar para a aba de "Feedback" após o envio
    showTab("feedback");
  }, 5000); // 5 segundos (5000 milissegundos)
}

// Mostrar a aba "Envios" por padrão
showTab("envios");
