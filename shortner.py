import requests

mean_txt = "Something broke slugger maybe try later or see a ophthalmologist (google it)"

def shorten_url(long_url):

    if not '.' in long_url:
        return "I ain't a mind reader, where Da Link? 🙄 that ain't a link"

    try:
        url = f"http://tinyurl.com/api-create.php?url={long_url}"
        response = requests.get(url)
        return_val = response.status_code
        print(response.status_code)
        if return_val == 200:
            return response.text
        elif return_val == 400:
            return mean_txt
        elif return_val == 422:
            return "URL is probably disabled for Reasons so can't convert this one"
        else:
            return f"{response.text} : {return_val}"
    except:
        return mean_txt

if __name__ == "__main__":

    long_url = "www.example.com"
    short_url = shorten_url(long_url)
    print(short_url)