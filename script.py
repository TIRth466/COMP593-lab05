from dad_jokes_api import search_dad_jokes
from pastebin_api import post_new_paste
import sys

def main():
    search_term=get_search_term()

    jokes_list=search_dad_jokes(search_term)
    
    if jokes_list:
       title, body_text=get_paste_content(jokes_list,search_term)
       paste_url=post_new_paste(title,body_text)
       print(f"URL of jokes paste: {paste_url}")

    
    return

def get_search_term():
   num_param=len(sys.argv)-1
   if num_param>0:
      sys.argv[1]
      return sys.argv[1]
      
   else:
      print("Error: Missing search term")
      
      
   
  
def get_paste_content(jokes_list,search_term):
   
   title=f'Dad jokes containing the term "{search_term}"'
   divider = '\n' + ('*' * 40) + '\n' 
   body_text = divider.join(jokes_list)

   return title, body_text
   
if __name__=="__main__":
 main()