<script>
  import perrococinero from "$lib/assets/perrococinero.png";
  import Bowl from "$lib/assets/bowl.png";

  let questions = [
    { id: 1, text: "What year did World War II begin?" },
    { id: 2, text: "What is the basic unit of life?" },
    { id: 3, text: "What was the significance of the Magna Carta?" },
    { id: 4, text: "Who painted the Mona Lisa?" },
    { id: 5, text: "What is the capital of Australia?" },
    {
      id: 6,
      text: "What is the function of red blood cells in the human body?",
    },
    { id: 7, text: "Who wrote the novel Pride and Prejudice?" },
    { id: 8, text: "Who discovered the Americas in 1492?" },
    { id: 9, text: "Which artist is known for creating the sculpture David?" },
    { id: 10, text: "In which country is the Great Wall located?" },
    { id: 11, text: "What is the difference between mitosis and meiosis?" },
    {
      id: 12,
      text: "Which European country colonized most of Africa during the period of imperialism?",
    },
  ];
  let selectedQuestions = [];

  function toggleQuestion(id) {
    const questionIndex = selectedQuestions.findIndex((q) => q === id);
    if (questionIndex === -1) {
      selectedQuestions = [...selectedQuestions, id];
    } else {
      selectedQuestions = selectedQuestions.filter((q) => q !== id);
    }
  }
</script>

<!-- -------------------- -->

<div class="m-10">
  <div class="w-full bg-lime-400 px-10 rounded-lg items-center py-10">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="w-[50%]">
        <img src={perrococinero} alt="perrito cocinando " />
      </div>
      <div class="w-[80%]">
        <h1 class="text-5xl font-bold">Hello! wof wof</h1>
        <p class="pt-6 text-xl">
          Thank you for playing with us! My name is Pedro, an I'm the quiz cook.
          Today, I'm going to help you have a more guided experience. Below, you
          will find two sections. The section on the left, is where you will
          find all the available categories for your quiz and the number of
          questions you can choose. Once you choose the details of your quiz
          the info will be displayed in the section on the right and once you are ready
          you can click on the button "Create my mix" to get your quiz ready.
          Time to play!!
        </p>
      </div>
    </div>
    <!---------- section ------------- -->
    <div class=" flex-col lg:flex-row-reverse w-full">
      <!-- ------1 column ---------- -->
      <div class="hero-content flex-col lg:flex-row-reverse">
        <!-- Sección de preguntas seleccionadas -->
        <div class="w-[100%]">
          <h3 class="py-6 text-xl font-bold">Preguntas seleccionadas:</h3>
          <div class="bg-lime-200 rounded-lg p-2 text-xl m-1">
            {#if selectedQuestions.length === 0}
              <p>No has seleccionado ninguna pregunta.</p>
            {:else}
              <ul class="m-1">
                {#each selectedQuestions as selectedQuestion}
                  <li class="m-1">
                    {questions.find((q) => q.id === selectedQuestion).text}
                  </li>
                {/each}
              </ul>
            {/if}
          </div>
          <div>
            <img src={Bowl} alt="bowl de mezcla " />
          </div>
        </div>
        <!-- Sección de selección de preguntas -->
        <div class="w-[100%]">
          <h2 class="py-6 text-xl font-bold">
            Selecciona tus preguntas favoritas:
          </h2>
          <div class="w-[80%] text-xl bg-lime-200 rounded-lg my-2 p-2">
            <ul class="m-1">
              {#each questions as question}
                <li
                  class="m-1"
                  on:click={() => toggleQuestion(question.id)}
                  class:selected={selectedQuestions.includes(question.id)}
                >
                  {question.text}
                </li>
              {/each}
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
