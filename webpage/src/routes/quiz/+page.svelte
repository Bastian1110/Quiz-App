<script>
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";

  let userToken;

  onMount(() => {
    if (typeof localStorage !== "undefined") {
      userToken = localStorage.getItem("token");
      if (!userToken) {
        goto("/login");
      }
    }
  });
  let quizStarted = false;

  let questions;
  let actualQuestionIndex = 0;
  let actualQuestion;

  let score = 0;

  let estado = 2;
  //0 correct, 1 incorrect, 2 pregunta

  const getQuestion = async () => {
    try {
      const response = await fetch(
        "http://137.184.20.150:8080/quiz/getQuestion",
        {
          method: "POST",
          headers: { "content-type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ id: questions[actualQuestionIndex] }),
        }
      );
      let data = await response.json();
      actualQuestion = data.question;
      estado = 2;
    } catch (err) {
      console.log(err);
    }
  };

  let quizFinished = false;

  const nextQuestion = async () => {
    if (actualQuestionIndex + 1 === questions.length) {
      quizFinished = true;
      estado = 3;
    } else {
      actualQuestionIndex = actualQuestionIndex + 1;
      await getQuestion();
    }
  };

  const answerQuestion = async (index) => {
    try {
      const response = await fetch(
        "http://137.184.20.150:8080/quiz/answerQuestion",
        {
          method: "POST",
          headers: {
            "content-type": "application/x-www-form-urlencoded",
            "x-access-token": userToken,
          },
          body: new URLSearchParams({
            id: questions[actualQuestionIndex],
            answer: index,
          }),
        }
      );
      let data = await response.json();
      if (data.result == 0) {
        estado = 0;
        score = score + data.points;
      }
      if (data.result == 1) {
        estado = 1;
      }
    } catch (err) {
      console.log(err);
    }
  };

  let nQuestions = 1;
  const beginQuiz = async () => {
    console.log(nQuestions);
    try {
      const response = await fetch(
        "http://137.184.20.150:8080/question/createQuiz",
        {
          method: "POST",
          headers: { "content-type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ questions: nQuestions }),
        }
      );
      let data = await response.json();
      if (data.error === 0) {
        questions = data.questions;
        await getQuestion();
        quizStarted = true;
      }
    } catch (err) {
      console.log(err);
    }
  };
</script>

<main class="grid grid-cols-6 m-10 bg-purple-500 rounded-xl">
  <h1 class="font-bold text-white text-6xl m-6 col-span-4">Quiz</h1>
  <span class="font-bold text-[#e1ffc2] text-4xl col-start-5 m-6 col-span-2"
    >Score : {score}</span
  >
  {#if !quizStarted}
    <div class="col-span-3 mx-12">
      <span class="font-bold text-2xl text-white"
        >How many questions do you want to answer?</span
      >
      <input
        bind:value={nQuestions}
        type="range"
        min="1"
        max="10"
        class="range mx-2"
        step="1"
      />
      <div
        class="w-full flex justify-between px-2 font-bold text-xl text-white"
      >
        <span>1</span>
        <span>2</span>
        <span>3</span>
        <span>4</span>
        <span>5</span>
        <span>6</span>
        <span>7</span>
        <span>8</span>
        <span>9</span>
        <span>10</span>
      </div>
      <div class="w-full text-center items-center justify-center">
        <button on:click={beginQuiz} class="btn btn-accent ml-10 my-6"
          >Begin!</button
        >
      </div>
    </div>
  {/if}
  {#if quizStarted && estado === 2}
    <div class="col-span-6 grid grid-cols-2 gap-2">
      <h2 class="font-bold text-2xl mx-8 my-2 text-white col-span-2">
        {actualQuestion.question}
      </h2>
      {#each actualQuestion.answers as answer, index}
        <button
          on:click={(e) => {
            e.preventDefault();
            answerQuestion(index);
          }}
          class="text-center hover:scale-110 active:bg-blue-300 hover:bg-blue-600 transition-all duration-200 bg-blue-500 text-white font-bold m-4 rounded-lg py-8 px-2"
        >
          {answer}
        </button>
      {/each}
    </div>
  {/if}
  {#if quizStarted && estado === 0}
    <div
      class="w-full bg-emerald-400 text-center text-white font-bold text-4xl col-span-4 col-start-2 py-12 my-4 rounded-lg"
    >
      Correct! 😌
    </div>
    <button
      class="btn btn-primary col-span-2 col-start-3 my-5"
      on:click={async (e) => {
        e.preventDefault();
        await nextQuestion();
      }}>Next</button
    >
  {/if}
  {#if quizStarted && estado === 1}
    <div
      class="w-full bg-rose-500 text-center text-white font-bold text-4xl col-span-4 col-start-2 py-12 my-4 rounded-lg"
    >
      Inorrect! 🥺
    </div>
    <button
      class="btn btn-primary col-span-2 col-start-3 my-5"
      on:click={async (e) => {
        e.preventDefault();
        await nextQuestion();
      }}>Next</button
    >
  {/if}
  {#if quizFinished}
    <div
      class="w-full bg-violet-400 text-center col-span-4 col-start-2 py-12 my-4 rounded-lg"
    >
      <h2 class="text-white font-bold text-4xl">Congratulations! 🥳</h2>
      <span class="text-white text-2xl">Your final score is : {score}</span>
    </div>
    <button
      class="btn btn-primary col-span-2 col-start-3 my-5"
      on:click={(e) => {
        e.preventDefault();
        goto("/");
      }}>Check Leader Board</button
    >
  {/if}
</main>
