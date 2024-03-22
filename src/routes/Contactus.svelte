<script>
 let Parameter = {
        "username":"",
        "message":"",
    };

 function gosubmit(){

 }

</script>
<div class="h-screen bg-cyan-700 flex justify-center">
<div class="flex w-full max-w-sm space-x-3">
    <div class="w-full max-w-2xl px-5 py-10 m-auto mt-24 bg-white rounded-lg shadow dark:bg-gray-800">
        <div class="my-6 text-3xl font-light text-center text-gray-800 dark:text-white">
            Inform us !
        </div>
        <div class="grid max-w-xl m-auto">
            <div class="col-span-2 pb-1">
                <div class=" relative ">
                </div>
            </div>
            <div class="col-span-2">
                <label class="text-gray-700" for="name">
                            <textarea class="flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 rounded-lg text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent" placeholder="Enter your comment" name="comment" rows="7" cols="50" bind:value={Parameter["message"]}/>

                </label>
            </div>
            <div class="col-span-2 text-right">
                <button type="submit" class="py-2 px-4  bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg " on:click="{gosubmit}">
                    Send
                </button>
            </div>
        </div>
    </div>
</div>
</div>
