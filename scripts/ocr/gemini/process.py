from google import genai
import os
import glob
from natsort import natsorted
#from pdf2image import convert_from_path

PROMPT = '''You are a world-class OCR engine. Output only text from the image. 
Do not answer questions yourself. Make sure to extract ALL text from the image.
If a word is italicized, please surround it with asterisks like this: *word*.'''
#Do not include page numbers, line numbers, or page headers.

in_jpg_folder = '../../data/imgs/Exercises_in_latin_prosody/Exercises_in_Latin_Prosody_and_Versifica'
out_folder = '../../data/raw_text/Exercises_in_latin_prosody'
do_subfolders = False
save_pages_separately = True

page_range = [65,67]

with open('gemini-key.txt', 'r') as file:
    gemini_key = file.read().strip()


def prep_image(client,image_path):
        sample_file = client.files.upload(file=image_path)
        return sample_file

def extract_text_from_image(client,image_path,prompt,image_name):
    response = client.models.generate_content(contents=[image_path,prompt], model="gemini-1.5-pro")
    try:
        return response.text
    except:
        print("FAIL PAGE "+image_name)
        return "FAIL PAGE " + image_name

def gemini(folder_path,out_dir,do_subfolders=True):
    '''  
    folder_path: path to parent directory, with subfolders of images. 
    each subfolder is a name of a document, and inside are its pages as images.

    out_dir: path to output directory. All pages for one doc will be written to a single txt file.
    '''
    
    client = genai.Client(api_key = gemini_key)
    os.makedirs(out_dir, exist_ok=True)

    if do_subfolders:
        subfolders = glob.glob(folder_path+"/*")
    else:
        subfolders = [folder_path]
    
    for subfolder in subfolders:
        print(subfolder)
        doc_name = subfolder.split('/')[-1]
        image_names = natsorted(glob.glob(subfolder+"/*.jpg"))
        #image_names_reorder = []
        #prefix = image_names[0][:image_names[0].find('_')]
        #for i in range(0,len(image_names)):
        #    image_names_reorder.append(prefix+'_'+str(i)+'.jpg')
        image_names_reorder = image_names
        
        print('  image names: ',image_names_reorder)
        if not save_pages_separately:
            out_f = open(out_dir+"/" + doc_name + ".txt", "w",encoding='utf-8')
            print('  out_f: ',out_f)
        else: 
            out_f_prefix = out_dir+"/" + doc_name + "_"

        if page_range:
            image_names_reorder = [subfolder + f"/{i}.jpg" for i in range(page_range[0],page_range[1]+1)]
            

        for image_name in image_names_reorder:
            img_num = image_name.split('/')[-1].split('.')[0]
            
            sample_file = prep_image(client,image_name)
            text = extract_text_from_image(client,sample_file,PROMPT,image_name)
            if text and not save_pages_separately:
                out_f.write(text+'\n')
                out_f.flush()
                print(image_name+" is done")
            elif text and save_pages_separately:
                with open(out_f_prefix+img_num+".txt", "w",encoding='utf-8') as out_f:
                    out_f.write(text+'\n')
                    out_f.flush()
                    print(image_name+" is done")
            else:
                print("fail on "+image_name)

gemini(in_jpg_folder,out_folder,do_subfolders)