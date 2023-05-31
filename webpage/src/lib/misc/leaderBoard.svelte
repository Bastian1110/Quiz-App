<script>
  import { onMount } from "svelte";
  import uno from "$lib/assets/uno.jpeg";
  import perro from "$lib/assets/perritoganador.png";

  let data;
  let top;

  onMount(async () => {
    try {
      const response = await fetch("http://137.184.20.150:8080/user/getTop");
      if (response.ok) {
        data = await response.json();
        top = data.top;
        console.log(top);
      } else {
        throw new Error("Request failed");
      }
    } catch (error) {
      console.error(error);
    }
  });
</script>

<div class="bg-[#a3ffa0] m-10 rounded-lg pb-10 grid grid-cols-6 gap-4">
  <div class="col-span-6">
    <h1 class="text-5xl font-bold text-left m-10 mb-4 text-indigo-500 w-full">
      LeaderBoard
    </h1>
    <p
      class="text-left justify-normal m-10 mb-4 mt-0 text-xl text-indigo-400 w-full"
    >
      Here you will find in what position you are, keep playing and be the
      number one in the table.
    </p>
  </div>
  <div class="col-span-4 m-10 mt-0">
    {#if data}
      <table class="table w-full">
        <!-- head -->
        <thead>
          <tr>
            <th>Avatar</th>
            <th>Name</th>
            <th>Place</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {#each top as user, index}
            <tr class="hover">
              <th>
                <div class="mask mask-squircle w-12 h-12">
                  <img src={uno} alt="uno" />
                </div>
              </th>
              <td>{user.username}</td>
              <td>{index + 1}st</td>
              <td>{user.score}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    {/if}
  </div>
  <div class="col-span-2 col-start-5 w-full h-auto">
    <img src={perro} alt="perrito" />
  </div>
</div>
