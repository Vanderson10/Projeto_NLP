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
  loadingDiv.id = "loading"; // Adicione um ID para facilitar a manipulação
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

  // Obtenha o conteúdo da redação do textarea
  const redacaoTexto = document.getElementById("redacao").value;

  // Crie um objeto com os dados da redação
  const redacaoJSON = { redacao: redacaoTexto };

  // Faça a requisição POST para o servidor
  fetch("http://127.0.0.1:5000/corrigir_redacao", {
    method: "POST",
    body: JSON.stringify(redacaoJSON),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((feedback) => {
      // Remover o GIF e o texto após a conclusão
      loadingDiv.parentNode.removeChild(loadingDiv);
      document.getElementById("feedbackChat").innerText = feedback.correcao;
    })
    .catch((error) => {
      console.error("Erro ao enviar a redação: " + error);
      // Lide com o erro, se necessário
    })
    .finally(() => {
      loadingDiv.style.display = "none";
      showTab("feedback");
    });
}

// Mostrar a aba "Envios" por padrão
showTab("envios");
