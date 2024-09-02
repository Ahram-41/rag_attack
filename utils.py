import json
def json2txt(file):
    path = 'chat-target/Q-R-T-'
    with open(f"./Inputs&Outputs/{path}/{file}.json", 'r', encoding='utf-8') as f:
            all_prompts = json.loads(f.read())

    with open(f"./Inputs&Outputs/{path}/{file}.txt", 'w', encoding='utf-8') as f_p:
        print(f"start to write {file}")
        f_p.write(json.dumps(all_prompts))
        print(f"{file} written")

if __name__ == "__main__":
    json2txt("outputs-llama-2-7b-chat-0.6-0.9-4096-256-1")
    # json2txt("context")
    # json2txt("question")
    # json2txt("prompts")
    # json2txt("sources")