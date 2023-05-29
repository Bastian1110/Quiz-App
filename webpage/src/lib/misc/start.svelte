<script>
  import bowl from "$lib/assets/bowl.png";
</script>

<div class="m-10">
  <div class="w-full bg-sky-400 px-10 rounded-lg items-center py-10">
    <div>
      <h1 class="text-3xl font-bold hover:text-sky-200">Second Step</h1>
      <p class="text-2xl mx-4 mt-3">
        Now choose the number of questions you want in your quizz mix
      </p>
    </div>
    <div class="grid grid-cols-2 gap-7">
      <div>
        <img
          class="pt-2 pl-10 w-[100%] text-center justify-center items-center"
          src={bowl}
          alt="perro inteligente "
        />
      </div>
      <div class="p-32 grid grid-cols-6 gap-7">
        <button class="text-center"> 5 </button>
        <button class="text-center"> 6 </button>
        <button class="text-center"> 7 </button>
        <button class="text-center"> 8 </button>
        <button class=""> 9 </button>
        <button class=""> 10 </button>
      </div>
    </div>
    <div>
        <button> Start Quizz  </button>
    </div>
  </div>
</div>

<style>
 button {
  position: relative;
  display: inline-block;
  padding: 15px 30px;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  letter-spacing: 1px;
  text-decoration: none;
  color: #451ccd;
  background: transparent;
  cursor: pointer;
  transition: ease-out 0.5s;
  border: 2px solid #451ccd;
  border-radius: 10px;
  box-shadow: inset 0 0 0 0 #451ccd;
}

button:hover {
  color: white;
  box-shadow: inset 0 -100px 0 0 #5325e9;
}

button:active {
  transform: scale(0.9);
}
</style>
