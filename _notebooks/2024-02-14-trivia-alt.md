<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Geography Trivia Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px;
    }
    #question-container {
      max-width: 600px;
      margin: 20px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      background-color: #f5f5f5;
    }
    #result {
      font-weight: bold;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Geography Trivia Game</h1>
  <div id="question-container">
    <p id="question"></p>
    <div id="options"></div>
    <button onclick="checkAnswer()">Submit Answer</button>
  </div>
  <div id="result"></div>

  <script>
    const questions = [
      {
        question: "What is the capital of France?",
        options: ["Berlin", "Madrid", "Paris", "Rome"],
        correctAnswer: "Paris"
      },
      {
        question: "Which river is the longest in the world?",
        options: ["Amazon", "Nile", "Yangtze", "Mississippi"],
        correctAnswer: "Nile"
      },
      {
        question: "In which continent is Australia located?",
        options: ["Asia", "Europe", "Australia", "North America"],
        correctAnswer: "Australia"
      }
    ];

    let currentQuestion = 0;
    let score = 0;

    function displayQuestion() {
      const questionElement = document.getElementById("question");
      const optionsContainer = document.getElementById("options");

      questionElement.textContent = questions[currentQuestion].question;

      optionsContainer.innerHTML = "";
      questions[currentQuestion].options.forEach((option, index) => {
        const button = document.createElement("button");
        button.textContent = option;
        button.onclick = () => selectAnswer(option);
        optionsContainer.appendChild(button);
      });
    }

    function selectAnswer(selectedOption) {
      const correctAnswer = questions[currentQuestion].correctAnswer;
      const resultElement = document.getElementById("result");

      if (selectedOption === correctAnswer) {
        score++;
        resultElement.textContent = "Correct! Well done!";
      } else {
        resultElement.textContent = `Wrong! The correct answer is ${correctAnswer}.`;
      }

      currentQuestion++;

      if (currentQuestion < questions.length) {
        displayQuestion();
      } else {
        showFinalScore();
      }
    }

    function showFinalScore() {
      const questionContainer = document.getElementById("question-container");
      questionContainer.innerHTML = `<p>Your final score is: ${score} out of ${questions.length}</p>`;
    }

    function checkAnswer() {
      const selectedOption = document.querySelector("button:focus").textContent;
      selectAnswer(selectedOption);
    }

    displayQuestion();
  </script>
</body>
</html>
