<script>
  import libros from "$lib/assets/libros.png";
  import Footer from "./footer.svelte";
</script>

<div class="m-10">
  <div class=" w-sm bg-teal-300 px-10 rounded-lg items-center">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <img src={libros} class="max-w-sm rounded-lg" />
      <div>
        <h1 class="text-5xl font-bold">Welcome to the best quizz App</h1>
        <p class="py-6 text-xl">
          Here you can find a variety of questions to test yourself, you can
          select them to make it your most personalized quiz :D
        </p>
        <button class="btn btn-primary">Get Started</button>
      </div>
    </div>
  </div>
</div>

<Footer />
