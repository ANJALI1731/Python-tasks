def detect_city(user_input):
    cities = ["mumbai", "delhi", "bangalore", "kolkata", "hyderabad", "pune", "coimbatore", "madurai", "chennai"]
    user_input = user_input.lower()
    for city in cities:
        if city in user_input:
            return city
    return "chennai"  # default

def get_college_answer(user_input):
    user_input = user_input.lower()
    city = detect_city(user_input)

    keyword_map = {
        "top colleges": ["top college", "top colleges", "best college", "best colleges", "top institutes", "best institutes"],
        "engineering colleges": ["engineering colleges", "engineering college", "b.tech", "be college"],
        "commerce colleges": ["commerce colleges", "bcom colleges", "b.com college"],
        "bba": ["bba", "bba colleges", "bba course"],
        "bcom": ["bcom", "b.com", "bcom course"],
        "cutoff": ["cutoff", "cut off", "minimum marks", "admission marks"],
        "fees": ["fees", "fee", "tuition fee", "college fee"],
        "hostel": ["hostel", "accommodation", "hostel fees"],
        "courses": ["courses", "programs", "subjects", "degree"],
        "reviews": ["reviews", "rating", "student feedback"],
        "ssn": ["ssn", "ssn college", "ssn engineering"],
        "cit": ["cit", "chennai institute of technology"],
        "rit": ["rit", "rajalakshmi institute of technology"],
        "rec": ["rec", "rajalakshmi engineering college"]
    }

    qa_data = {
        "top colleges": {
            "chennai": "Top colleges in Chennai: Loyola, MCC, Stella Maris, Presidency College.",
            "default": f"Top colleges in {city.title()} include reputed institutions."
        },
        "engineering colleges": {
            "chennai": "Engineering colleges in Chennai: Anna University, SSN, SRM, Sathyabama.",
            "default": f"Engineering colleges in {city.title()} include both private and govt institutions."
        },
        "commerce colleges": {
            "chennai": "Commerce colleges: Loyola, MCC, Ethiraj, M.O.P.",
            "default": f"Commerce colleges in {city.title()} include top commerce schools."
        },
        "bba": {
            "chennai": "BBA colleges: M.O.P. Vaishnav, DG Vaishnav, Loyola.",
            "default": f"BBA programs in {city.title()} are widely available."
        },
        "bcom": {
            "chennai": "Top B.Com colleges: Loyola, MCC, Ethiraj.",
            "default": f"B.Com courses are available in many colleges in {city.title()}."
        },
        "cutoff": {
            "chennai": "Cutoffs vary: Loyola ~90%, MCC 85–95%, SSN ~TNEA rank under 200.",
            "default": f"Cutoffs in {city.title()} depend on college and course."
        },
        "fees": {
            "chennai": "Fees: Loyola ~₹25k, SRM ~₹2.5L, SSN ~₹1L/year.",
            "default": f"Fees vary in {city.title()} from ₹20k to ₹2L depending on college."
        },
        "hostel": {
            "chennai": "Most colleges like SRM, Sathyabama, Loyola offer hostel facilities.",
            "default": f"Hostel facilities available in many colleges of {city.title()}."
        },
        "courses": {
            "chennai": "Courses: B.A., B.Sc., BBA, B.Com, B.Tech, M.A., MBA, MCA.",
            "default": f"Courses offered in {city.title()} include UG and PG programs."
        },
        "reviews": {
            "chennai": "Reviews: Loyola and MCC are highly rated for academics and campus.",
            "default": f"Reviews for colleges in {city.title()} vary. Visit forums for info."
        },
        "ssn": "SSN College: Top private engineering college in Chennai. Excellent placements.",
        "cit": "CIT: Fast-growing engineering college with good industry tie-ups.",
        "rit": "RIT: Offers B.E./B.Tech. Good infrastructure, affiliated to Anna University.",
        "rec": "REC: Rajalakshmi Engineering College. NAAC A+ accredited, good placements."
    }

    responses = []

    for topic, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword in user_input:
                if isinstance(qa_data[topic], dict):
                    answer = qa_data[topic].get(city, qa_data[topic].get("chennai"))
                else:
                    answer = qa_data[topic]
                responses.append(answer)
                break

    if responses:
        return "\n\n".join(set(responses))
    else:
        return "Sorry, I couldn't find an answer. Try asking about top colleges, fees, courses, or hostels."

# ----------------------
# Main chatbot loop
# ----------------------
if __name__ == "__main__":
    print("\U0001F393 College Search Chatbot")
    print("Ask about top colleges, courses, cutoffs, fees, hostels, etc. Type 'exit' to quit.\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Bot: Goodbye! Best wishes for your future!")
            break
        response = get_college_answer(query)
        print("Bot:", response + "\n")
