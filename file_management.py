import os
import logging


logging.basicConfig(
    filename = 'file_management.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def list_files(directory):
    try:
        files = os.listdir(directory)

        all_files = []

#  files = [item for item in items if os.path.isfile(os.path.join(directory, item))]

        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                all_files.append(file)
       
       
        if all_files:
            print("Files in the directory:")
            for file in all_files:
                print(f" - {file}")
        else:
            print("No files found in the directory.")

        logging.info(f"Listed files in directory: {directory}")

    except FileNotFoundError:
        print("Error: The directory does not exist.")
        logging.error(f"Directory not found: {directory}")
    except PermissionError:
        print("Error: Permission denied to access the directory.")
        logging.error(f"Permission denied accessing directory: {directory}")
    except Exception as e:
        print(f"The following error occurred: {str(e)}")     
        logging.error(f"The following error occurred: {str(e)}")


def create_file(directory):
    try:
        file_name = input("Enter the name of the file you want to create: ").strip()

        file_path = os.path.join(directory,file_name)

         
        with open(file_path,'w') as file:
            pass

        print(f"File {file_name} successfully created")
        logging.info(f"File {file_path} successfully created")

    except FileExistsError:
        print("Error: File already exists.")
        logging.error(f"Failed to create file (already exists): {file_path}")
    except PermissionError:
        print("Permission denied ")
        logging.error("Permission denied")
    except Exception as e:
        print(f"The following error occurred: {str(e)}")     
        logging.error(f"The following error occurred: {str(e)}")


def delete_file(directory):
    try:
        file_name = input("Enter the name of the file you want to delete: ")
        file_path = os.path.join(directory,file_name)

        os.remove(file_path)
        print("File deleted successfully!")
        logging.info(f"File {file_path} deleted successfully")

    except FileNotFoundError:
        print("Error: File not found")
        logging.error(f"File {file_path} not found")
    except PermissionError:
        print("Permission denied to delete the file")
        logging.error(F"No Permission to delete the file {file_path} ")
    except Exception as e:
        print(f"The following error occurred: {str(e)}")     
        logging.error(f"The following error occurred: {str(e)}")

def rename_file(directory):
    try:

        old_name = input("Enter the old name of the file: ")
        new_name = input("Enter the new name of the file: ")

        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)

        print("File renamed successfully.")
        logging.info("File renamed successfully.")

    except FileNotFoundError:
        print("File not found")
        logging.error(f"File {old_path} not found")

    except FileExistsError:
        print("File with new name already exists")
        logging.error(f"File {new_path} already exists")
    
    except PermissionError:
        print("Permission denied to rename file")
        logging.error(f"Permission denied to rename")
    
    except Exception as e:
        print(f"The following error occurred: {str(e)}")     
        logging.error(f"The following error occurred: {str(e)}")


def search_file(directory):
    try:
        search_term = input("Enter the search term: ")

        files = os.listdir(directory)

        matches = []

        for file in files:
            if os.path.isfile(os.path.join(directory, file)) and search_term in file:
                matches.append(file)

        if matches:
            print("Matching files found")

            for match in matches:
                print(f"- {match}")
        else:
            print("No matching files found.")

        logging.info(f"Searched for term '{search_term}' in directory: {directory}")

    except PermissionError:
        print("Error: Permission denied to access the directory.")
        logging.error(f"Permission denied accessing directory during search: {directory}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Error searching files in {directory}: {e}")


def main():

    print("Welcome to Python File Manager App")

    directory = input("Enter the directory path you want to manage: ").strip()
    
    # strip(): Removes any leading/trailing whitespace from the input.


    # Check if the directory exists
    if not os.path.exists(directory):
            print("Error: Directory not found! ")
            return  # Exit the program


    while True:
        print("\nAvailable Commands")
        print("'list' to List all files")
        print("'create' to Create a file")
        print("'delete' to Delete a file")
        print("'rename' to Rename a file")
        print("'search' to Search a file")
        print("'exit' to Exit the program")

        
        command = input("Enter your choice: ").strip().lower()

        if command == 'list':
            list_files(directory)

        elif command == 'create':
            create_file(directory)

        elif command == "delete":
            delete_file(directory)

        elif command == 'rename':
            rename_file(directory)

        elif command == "search":
            search_file(directory)

        elif command == 'exit':
            print("Thank you for using the File Management App. Bye!")
            break

        else:
            print("Invalid command. Please enter one of the following: 'list' , 'create' , 'delete' , 'rename' , 'search'  ")

    

if __name__ == "__main__":
    
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting now..")
        logging.info("Program interrupted by user.")