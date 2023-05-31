<script>
  import libros from "$lib/assets/libros.png";
</script>

<div class="m-10">
  <div class=" w-sm bg-secondary px-10 rounded-lg items-center">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <img
        src={libros}
        class="max-w-sm rounded-lg w-[50%] md:w-[80%]"
        alt="Libros"
      />
      <div>
        <h1 class="text-5xl font-bold text-[#d1fff4]">
          Welcome to the best Quizz App
        </h1>
        <p class="py-6 text-xl text-[#ffffff] font-semibold">
          Here you can find a variety of questions to test yourself, you can
          select them to make it your most personalized quiz.
        </p>
        <a href="/quiz" class="btn btn-accent">Answer a Quiz</a>
      </div>
    </div>
  </div>
</div>
