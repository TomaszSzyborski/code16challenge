import justpy as jp
import asyncio
import requests as r

pokemons, page = ((r.get(it["url"]).json()["sprites"]["front_default"], f"{it['name'].title()} pomaga!", "A ty?") for it
                  in r.get(f"https://pokeapi.co/api/v2/pokemon?limit=2000").json()["results"]), jp.QuasarPage()
div = jp.QImg(classes='absolute-center', style="width: 50vw; height: 90vh", a=page)
caption_top, caption_bottom = [jp.QDiv(classes=f"absolute-{pos} text-center text-h3") for pos in ["top", "bottom"]]

async def show_pokemon():
    for pokemon in pokemons:
        div.src, caption_top.text, caption_bottom.text = pokemon
        div.delete_components() or all(map(lambda it: div.add_component(it), [caption_top, caption_bottom]))
        jp.run_task(page.update()) or await asyncio.sleep(2)

jp.justpy(lambda: page, startup=lambda: jp.run_task(show_pokemon()))