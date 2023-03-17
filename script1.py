from pastebin_api import post_new_paste
from poke_api import get_info_poke
import sys




def main():
    name=get_poke_name()
    info=get_info_poke(name)
    #print(info)

    if info:
       title, body_text=poke_paste(info)
       paste_url=post_new_paste(title,body_text,'1M')
       print(paste_url)
    return

def get_poke_name():
    num_params=len(sys.argv)-1
    if num_params>0:
        return sys.argv[1]
    else:
        print(f"Error: Missing parameters.")
        

def poke_paste(info):
    name=info['name'].capitalize()
    abilities = []
    for ability in info['abilities']:
        abilities.append(ability['ability']['name'])
    print(abilities)
    abilities_list='\n '.join(abilities)
    title= f"{name}s Abilities"
    body=abilities_list

    return title,body 




if __name__ == '__main__':
    main()