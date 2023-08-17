import os, shutil, requests, datetime ,subprocess,sys
from bs4 import BeautifulSoup 



# 2 directories same or not?
def are_directories_equal(dir1, dir2):
    abs_dir1 = os.path.abspath(dir1)
    abs_dir2 = os.path.abspath(dir2)
    return abs_dir1 == abs_dir2

def run_git_command(command):
    try:
        print(command)
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return result.stderr.strip()
    except Exception as e:
        return str(e)



if len(sys.argv) > 1:
    input_text = sys.argv[1]
    file_name = input_text[2:] if input_text.startswith('.\\') or input_text.startswith('./') else input_text
    print(file_name)
else:
    print("No input provided.")


file_path = os.path.join(os.getcwd(), file_name)

with open(file_path, 'r') as file:
    file_content = file.readline().strip()   # pull out the link from file Read
    print(file_content)


#file extension define

file_extension = os.path.splitext(file_path)[1]
print("File extension:", file_extension)

if file_extension == ".cpp" and file_content[:2] == "//":
    
    language = "C++"  #programming language
    print("Programming Language:", language)


    # URL of the page you want to scrape
    url = file_content[2:].strip()
    print("The Platform link:", url)

    if "codeforces" in url:
        platform = "codeforeces"  # Contest platform
        print("The platform is:", platform )
    else:
        print("Platform not found.")

    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
  
    # Find the outer div with a specific class
    outer_div = soup.find("div", class_="header")

    # Check if the outer div was found
    if outer_div:
        # Find the inner div with the specific class within the outer div
        inner_div = outer_div.find("div", class_="title")

        # Check if the inner div was found
        if inner_div:
            # Get the text content of the inner div
            title_text = inner_div.get_text(strip=True)
            print("Probmlem Title:", title_text)
        else:
            print("Inner div not found.")
    else:
        print("Inner div not found.")

else:
    print("anoter file extension.")







# Get the current working directory and Root Directory
current_directory = os.path.join(os.getcwd(), file_name) 
#root_directory =   "H:\Programming-Contest-Coding" # need user input later
root_directory =   os.path.join("H:\Programming-Contest-Coding", title_text + file_extension)
print(current_directory)
print(root_directory)

if are_directories_equal(current_directory, root_directory):
    print("The directories are the same.")
else:
    print("The directories are different.")
    shutil.copy(current_directory, root_directory)
    os.chdir("H:\Programming-Contest-Coding")



#solution link
solution_link = "https://github.com/Hasib98/Programming-Contest-Coding/blob/main/" + title_text.replace(" ", "%20") + file_extension
print(solution_link)

current_date = datetime.datetime.now().date().strftime("%Y-%m-%d")

# Print the current date
print("Current date:", current_date)


print("Current working directory is:", os.getcwd())


#README file update.................


readme_file_path = os.path.join(os.getcwd(), "README.md") 
with open(readme_file_path, 'a') as file:
    table_data = "| ["+platform+"]("+url+") | "+title_text+" | [Link]("+solution_link+") | "+language+" | "+current_date+" |\n"
    print(table_data)
    file.write(table_data)

print(table_data)



# Git commands executions...........


git_command_add = ["git" , "add" , "README.md" ,title_text + file_extension]
output = run_git_command(git_command_add)
print(output)
print("-------------------------------")

git_command_commit = ["git" , "commit" ,"-m" , language ]
output = run_git_command(git_command_commit)
print(output)
print("-------------------------------")

git_command_push = "git push"
output = run_git_command(git_command_push)
print(output)


