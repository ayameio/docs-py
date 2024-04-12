import json
import re

apartments_path = "/assets/images/buildings/"
goods_path = "/assets/images/buildings/goods/"
materials_path = "/assets/images/buildings/materials/"
gemstones_path = "/assets/images/buildings/gemstones/"
decorations_path = "/assets/images/buildings/decorations/"
icons_path = "/assets/images/items/"

item_key_map = {
    "goldCoin": "Gold Coin",
    "goldBar": "Gold Bar",
    "diamond": "Diamond",
    "infusedBrick": "Infused Brick",
    "infusedLog": "Infused Log",
    "atom": "Atom",
    "neutron": "Neutron",
    "molecule": "Molecule",
}

with open('data.json', 'r') as json_file:
    # Load JSON data into a Python dictionary
    python_dict = json.load(json_file)

for k in python_dict:
    print(k)
    for j in python_dict[k]['nodes']:
        print(python_dict[k]['nodes'][j]['label'])
        print("Costs")
        for v in python_dict[k]['nodes'][j]['cost']:
            val = python_dict[k]['nodes'][j]['cost'][v]
            lab = item_key_map[v]
            icon = icons_path + v
            print(val, lab, icon)
        print("\n")
    print('-----------------')

def print_costs(dict):
    for v in dict:
        val = python_dict[k]['nodes'][j]['cost'][v]
        lab = item_key_map[v]
        icon = icons_path + v
        print(val, lab, icon)

print("GEN")

def gen_costs_labels(key, category):
    html = f"""

    """
    for c in python_dict[category]['nodes'][key]['cost']:
        html += f"<td>{item_key_map[c]}</td>\n"
    return html


def gen_costs_values(key, category):
    html = f"""

    """
    for c in python_dict[category]['nodes'][key]['cost']:
        html += f"<td>{python_dict[category]['nodes'][key]['cost'][c]}</td>\n"
    html.strip('\n')
    return html

def gen_images(key, category):
    html = f"""

    """
    for c in python_dict[category]['nodes'][key]['cost']:
        path = "/assets/images/items/"+c+".png"
        width = "width='64'"
        height = "height='64'"
        html += f"<td><img src={path} {width} {height}></td>'\n"
    html.strip('\n')
    return html

def remove_empty_lines(text):
    return re.sub(r'\n\s*\n', '\n', text)

def gen(category):
    category_paths = {
        "goodsProductions": "/assets/images/buildings/goods/",
        "materialsProductions": "/assets/images/buildings/materials/",
        "apartments": "/assets/images/buildings/apartments/",
        "decorations": "/assets/images/buildings/decorations/",
        "gemstoneProductions": "/assets/images/buildings/gemstones/"
    }
    html = f"""
    <table>
	<thead>
		<tr>
			<th style="text-align:center;"><p align="center" style="min-width: 96px; min-height: 96px;"><img src="/assets/images/icons/buildHammer.png" width="96" height="96">Building</p></th>
			<th style="text-align:center;"><p align="center" style="min-width: 96px; min-height: 96px;"><img src="/assets/images/icons/goldCoin.png" width="96" height="96"> Costs</p></th>
			<th style="text-align:center;"><p align="center" style="min-width: 96px; min-height: 96px;"><img src="/assets/images/icons/stopwatch.png" width="96" height="96"> Build Time</p></th>
			<th style="text-align:center;"><p align="center" style="min-width: 96px; min-height: 96px;"><img src="/assets/images/icons/sizeIcon.png" width="96" height="96"> Size</p></th>
			<th style="text-align:center;"><p align="center" style="min-width: 96px; min-height: 96px;"><img src="/assets/images/icons/vibeIcon.png" width="96" height="96"> Vibe</p></th>
		</tr>
	</thead>
    """
    for key in python_dict[category]['nodes']:
        
        lab = python_dict[category]['nodes'][key]['label']
        size = python_dict[category]['nodes'][key]['size']
        build_time = python_dict[category]['nodes'][key]['buildTime']
        vibe_points = python_dict[category]['nodes'][key]['vibePoints']

        image_path = f"{category_paths[category]}{key}.png"
        print(image_path)
        # gen_costs(key)
        html += f"""
        <tbody>
		<tr>
			<td>
            <tr>
                <td>
                    <table>
                        <thead>
                            <tr>
                                <th>{lab}</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <div style="width: 128px;"><img
                                            src="{image_path}" width="256"
                                            height="256"></div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td>
                    <table>
                        <thead>
                            <tr>
                                {gen_costs_labels(key, category)}
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                {gen_images(key, category)}
                            </tr>
                            <tr>
                                {gen_costs_values(key, category)}
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td>{build_time}</td>
                <td>{size}</td>
                <td>{vibe_points}</td>
            </tr>
        	</td>
		</tr>
		</tbody>
        """
    html += f"</table>"
    with open(f"{category}.md", "a") as md_file:
        md_file.write(html)
        
gen("goodsProductions")
gen("decorations")