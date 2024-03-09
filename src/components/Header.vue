<script setup>
</script>
<template>
	<header class="flex justify-between border-b border-slate-200 desktop:px-10 desktop:py-8 px-2 py-2.5 small:sticky small:top-0 small:z-10 small:bg-black select-none">

		<div class="flex items-center gap-4">
      <div class="border rounded-full bg-white desktop:w-[60px] desktop:h-[60px]">
        <img src="/logo.svg" alt="Logo" class="w-[60px]" />
      </div>

			<div>
				<h2 class="text-xl font-bold uppercase hidden desktop:block">ME2ME</h2>
				<p class="text-slate-500 hidden desktop:block">Produced by ME2ME Team</p>
			</div>
		</div>

		<ul class="flex itens-center gap-10">
      <li class="flex items-center gap-3 text-gray-400 hover:text-gray-200 transition delay-[30ms] cursor-pointer desktop:text-xl">
				<span>Фильтры</span>
			</li>

			<li class="flex items-center gap-3 text-gray-400 hover:text-gray-200 transition delay-[30ms] cursor-pointer desktop:text-xl">
				<img src="/profile.svg" alt="cart" class="hidden desktop:block w-[24px] h-[24px]"/>
				<span>Профиль</span>
			</li>
		</ul>

	</header>
</template>
