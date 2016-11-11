import requests
import json


def get_request(url):
    try:
        req = requests.get(url=url)
        results = json.loads(req.text)
        return results
    except:
        print("Something went wrong, check the url!")


def save_json(results, out_filename):
    with open('{}.json'.format(out_filename), 'w') as f:
        json.dump(results, f)


def complex_request_example(base, before, after, out_filename="complex"):
    results = []
    for i in range(1194):
        page = i + 1
        try:
            url = base.format(before, after, page)
            req = requests.get(url=url)
            results += json.loads(req.text)
        except:
            print("Stopped at: {}".format(i))
            break
    save_json(results, out_filename)


def main(url, out_filename):
    results = get_request(url)
    save_json(results, out_filename)


if __name__ == '__main__':
    url_basic = 'http://elections.huffingtonpost.com/pollster/api/polls.json'
    url_filter = 'http://elections.huffingtonpost.com/pollster/api/charts?state=CA'
    main(url_basic, "basic_request")
    main(url_filter, "filtered_request")
    before = '2012-11-06'
    after = '2008-11-04'
    base = "http://elections.huffingtonpost.com/pollster/api/polls.json?before={}&after={}&page={}"
    complex_request_example(base, before, after)
