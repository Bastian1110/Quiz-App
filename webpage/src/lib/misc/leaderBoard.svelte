<script>
  import uno from "$lib/assets/uno.jpeg";
  import dos from "$lib/assets/dos.jpeg";
  import tres from "$lib/assets/tres.jpeg";
  import cuatro from "$lib/assets/cuatro.jpeg";
  import cinco from "$lib/assets/cinco.jpeg";
  import perro from "$lib/assets/perritoganador.png";
</script>

<div class="bg-yellow-400 m-10 rounded-lg">
  <h1 class="text-5xl font-bold text-center mt-5 pt-4 hover:text-yellow-200">LeaderBoard</h1>
  <p class="text-center m-5 pt-4 text-xl">
    Here you will find in what position you are, keep playing and be the number
    one in the table.
  </p>

  <div class="hero-content flex-col lg:flex-row-reverse m-10 pb-10 ">
    <div class=" w-[40%] ">
      <img src={perro} alt="perrito" />
    </div>
    <table class="table w-full">
      <!-- head -->
      <thead>
        <tr >
          <th />
          <th>Name</th>
          <th>Place</th>
          <th>Points</th>
        </tr>
      </thead>
      <tbody>
        <!-- row 1 -->
        <tr class="hover">
          <th>
            <div class="mask mask-squircle w-12 h-12 ">
              <img src={uno} alt="uno" />
            </div>
          </th>
          <td>Sal Pique</td>
          <td>1st</td>
          <td>556</td>
        </tr>
        <!-- row 2 -->
        <tr class="hover">
          <th>
            <div class="mask mask-squircle w-12 h-12">
              <img src={dos} alt="dos" />
            </div>
          </th>
          <td>Pitches</td>
          <td>2nd</td>
          <td>482</td>
        </tr>
        <!-- row 3 -->
        <tr class="hover">
          <th>
            <div class="mask mask-squircle w-12 h-12">
              <img src={tres} alt="tres" />
            </div>
          </th>
          <td>La queso</td>
          <td>3rd</td>
          <td>423</td>
        </tr>
        <!-- row 4 -->
        <tr class="hover">
          <th>
            <div class="mask mask-squircle w-12 h-12">
              <img src={cuatro} alt="dos" />
            </div>
          </th>
          <td>Quetti</td>
          <td>4th</td>
          <td>368</td>
        </tr>
        <!-- row 5 -->
        <tr class="hover">
          <th>
            <div class="mask mask-squircle w-12 h-12">
              <img src={cinco} alt="dos" />
            </div>
          </th>
          <td>bebito fiu fiu</td>
          <td>5th</td>
          <td>305</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
