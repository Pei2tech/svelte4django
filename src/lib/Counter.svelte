<script>
  let count = 0;
  const increment = () => {
    count += 1;
  }
</script>

<span> show counter: {count} </span>
<button type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm"  on:click={increment}>
  Clicks
</button>

<style>

</style>
