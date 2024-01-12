import requests
import json

class GetPrograms:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_programs(self):
        URL = "https://data.cityofnewyork.us/resource/uvks-tn5n.json"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(URL, headers=headers)
        return response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            if "agency" in program:
                programs_list.append(program["agency"])

        return programs_list

if __name__ == "__main__":
    api_key = "https://api.thedogapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
    programs = GetPrograms(api_key)
    programs_schools = programs.program_school()

    for school in set(programs_schools):
        print(school)
