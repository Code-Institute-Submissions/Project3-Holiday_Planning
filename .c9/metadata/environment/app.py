{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["t"],"id":420}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["T"],"id":421}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":422}],[{"start":{"row":11,"column":0},"end":{"row":17,"column":56},"action":"insert","lines":["# Function to display landing page (Working)","@app.route('/')","def index():","    messages = get_flashed_messages()","    print(messages)","    results = db[ALBUMS].find({})","    return render_template(\"index.html\", data = results)"],"id":423}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":44},"action":"remove","lines":[" (Working)"],"id":424}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":[" "],"id":425}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":37},"action":"insert","lines":["()"],"id":426}],[{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":["S"],"id":427},{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"insert","lines":["a"]},{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"insert","lines":["m"]},{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"insert","lines":[";"]},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"remove","lines":["s"],"id":428},{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"remove","lines":[";"]}],[{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"insert","lines":["'"],"id":429},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"insert","lines":[" "],"id":430},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["c"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["o"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["d"]},{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":15},"action":"remove","lines":["@app.route('/')"],"id":431},{"start":{"row":19,"column":72},"end":{"row":20,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":33},"action":"remove","lines":["index"],"id":432},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["t"]},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["a"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["s"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["k"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["    messages = get_flashed_messages()","    print(messages)","    results = db[ALBUMS].find({})",""],"id":433}],[{"start":{"row":14,"column":41},"end":{"row":14,"column":55},"action":"remove","lines":["data = results"],"id":434},{"start":{"row":14,"column":41},"end":{"row":14,"column":68},"action":"insert","lines":["tasks=mongo.db.tasks.find()"]}],[{"start":{"row":14,"column":69},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":435},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":20},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":436}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[" "],"id":437},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":[" "]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":35},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":438}],[{"start":{"row":35,"column":41},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":439},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":4},"end":{"row":37,"column":0},"action":"insert","lines":["",""]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":4},"end":{"row":38,"column":0},"action":"insert","lines":["",""]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":39,"column":0},"action":"insert","lines":["",""]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "],"id":440}],[{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"remove","lines":[")"],"id":441},{"start":{"row":12,"column":45},"end":{"row":12,"column":46},"action":"remove","lines":["e"]},{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"remove","lines":["d"]},{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"remove","lines":["o"]},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"remove","lines":["c"]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":[" "]},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"remove","lines":["s"]},{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"remove","lines":["'"]},{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"remove","lines":["m"]},{"start":{"row":12,"column":37},"end":{"row":12,"column":38},"action":"remove","lines":["a"]},{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"remove","lines":["S"]},{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"remove","lines":["("]},{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"remove","lines":[" "]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"remove","lines":["f"],"id":442},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"remove","lines":[" "]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"remove","lines":["s"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"remove","lines":["i"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"remove","lines":["h"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"remove","lines":["t"]}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["F"],"id":443}],[{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":[" "],"id":444},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["T"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["O"]}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"remove","lines":["O"],"id":445},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"remove","lines":["T"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["t"],"id":446},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["o"]}],[{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"remove","lines":["f"],"id":447},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"remove","lines":[" "]},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"remove","lines":["s"]},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"remove","lines":["i"]},{"start":{"row":24,"column":3},"end":{"row":24,"column":4},"action":"remove","lines":["h"]},{"start":{"row":24,"column":2},"end":{"row":24,"column":3},"action":"remove","lines":["t"]}],[{"start":{"row":24,"column":2},"end":{"row":24,"column":3},"action":"insert","lines":["F"],"id":448}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["T"],"id":449},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["O"]}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["O"],"id":450},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":["T"]}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["t"],"id":451},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["o"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":[" "],"id":452}],[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["f"],"id":453},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":[" "]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["s"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["i"]},{"start":{"row":30,"column":3},"end":{"row":30,"column":4},"action":"remove","lines":["h"]},{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"insert","lines":["F"],"id":454}],[{"start":{"row":35,"column":41},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":455},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":4},"end":{"row":37,"column":0},"action":"insert","lines":["",""]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":456}],[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":457}],[{"start":{"row":38,"column":0},"end":{"row":41,"column":69},"action":"insert","lines":["# Function to fetch all our data in mongodb pass it back to tasks.html","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())"],"id":458}],[{"start":{"row":38,"column":64},"end":{"row":38,"column":65},"action":"remove","lines":["s"],"id":459},{"start":{"row":38,"column":63},"end":{"row":38,"column":64},"action":"remove","lines":["k"]},{"start":{"row":38,"column":62},"end":{"row":38,"column":63},"action":"remove","lines":["s"]},{"start":{"row":38,"column":61},"end":{"row":38,"column":62},"action":"remove","lines":["a"]},{"start":{"row":38,"column":60},"end":{"row":38,"column":61},"action":"remove","lines":["t"]}],[{"start":{"row":38,"column":60},"end":{"row":38,"column":61},"action":"insert","lines":["C"],"id":460},{"start":{"row":38,"column":61},"end":{"row":38,"column":62},"action":"insert","lines":["A"]},{"start":{"row":38,"column":62},"end":{"row":38,"column":63},"action":"insert","lines":["T"]},{"start":{"row":38,"column":63},"end":{"row":38,"column":64},"action":"insert","lines":["E"]},{"start":{"row":38,"column":64},"end":{"row":38,"column":65},"action":"insert","lines":["G"]},{"start":{"row":38,"column":65},"end":{"row":38,"column":66},"action":"insert","lines":["O"]},{"start":{"row":38,"column":66},"end":{"row":38,"column":67},"action":"insert","lines":["R"]},{"start":{"row":38,"column":67},"end":{"row":38,"column":68},"action":"insert","lines":["Y"]}],[{"start":{"row":38,"column":67},"end":{"row":38,"column":68},"action":"remove","lines":["Y"],"id":461},{"start":{"row":38,"column":66},"end":{"row":38,"column":67},"action":"remove","lines":["R"]},{"start":{"row":38,"column":65},"end":{"row":38,"column":66},"action":"remove","lines":["O"]},{"start":{"row":38,"column":64},"end":{"row":38,"column":65},"action":"remove","lines":["G"]},{"start":{"row":38,"column":63},"end":{"row":38,"column":64},"action":"remove","lines":["E"]},{"start":{"row":38,"column":62},"end":{"row":38,"column":63},"action":"remove","lines":["T"]},{"start":{"row":38,"column":61},"end":{"row":38,"column":62},"action":"remove","lines":["A"]},{"start":{"row":38,"column":60},"end":{"row":38,"column":61},"action":"remove","lines":["C"]}],[{"start":{"row":38,"column":60},"end":{"row":38,"column":61},"action":"insert","lines":["c"],"id":462},{"start":{"row":38,"column":61},"end":{"row":38,"column":62},"action":"insert","lines":["a"]},{"start":{"row":38,"column":62},"end":{"row":38,"column":63},"action":"insert","lines":["t"]},{"start":{"row":38,"column":63},"end":{"row":38,"column":64},"action":"insert","lines":["e"]},{"start":{"row":38,"column":64},"end":{"row":38,"column":65},"action":"insert","lines":["g"]},{"start":{"row":38,"column":65},"end":{"row":38,"column":66},"action":"insert","lines":["o"]},{"start":{"row":38,"column":66},"end":{"row":38,"column":67},"action":"insert","lines":["r"]},{"start":{"row":38,"column":67},"end":{"row":38,"column":68},"action":"insert","lines":["y"]}],[{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"remove","lines":["s"],"id":463},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"remove","lines":["k"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"remove","lines":["s"]},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"remove","lines":["a"]},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"remove","lines":["t"]}],[{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"insert","lines":["c"],"id":464},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"insert","lines":["a"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"insert","lines":["t"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"insert","lines":["e"]},{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"insert","lines":["g"]},{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"insert","lines":["o"]},{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"insert","lines":["r"]},{"start":{"row":39,"column":24},"end":{"row":39,"column":25},"action":"insert","lines":["y"]}],[{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"remove","lines":["s"],"id":465},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"remove","lines":["k"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"remove","lines":["s"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"remove","lines":["a"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["c"],"id":466},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["a"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["t"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["e"]},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["g"]},{"start":{"row":40,"column":13},"end":{"row":40,"column":14},"action":"insert","lines":["o"]},{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":["r"]},{"start":{"row":40,"column":15},"end":{"row":40,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":21,"column":41},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":474},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":8},"action":"insert","lines":["    "],"id":475}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"insert","lines":["    "],"id":476}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":16},"action":"insert","lines":["    "],"id":477}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":20},"action":"insert","lines":["    "],"id":478}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":24},"action":"insert","lines":["    "],"id":479}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":28},"action":"insert","lines":["    "],"id":480}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":28},"action":"remove","lines":["    "],"id":481}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":28},"action":"insert","lines":["    "],"id":482}],[{"start":{"row":28,"column":43},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":483},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"insert","lines":["    "],"id":484}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":12},"action":"insert","lines":["    "],"id":485}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":16},"action":"insert","lines":["    "],"id":486}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":20},"action":"insert","lines":["    "],"id":487}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":24},"action":"insert","lines":["    "],"id":488}],[{"start":{"row":29,"column":24},"end":{"row":29,"column":28},"action":"insert","lines":["    "],"id":489}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":490},{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""]},{"start":{"row":41,"column":0},"end":{"row":41,"column":1},"action":"insert","lines":["C"]},{"start":{"row":41,"column":1},"end":{"row":41,"column":2},"action":"insert","lines":["A"]}],[{"start":{"row":41,"column":2},"end":{"row":41,"column":3},"action":"insert","lines":["T"],"id":491},{"start":{"row":41,"column":3},"end":{"row":41,"column":4},"action":"insert","lines":["E"]},{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"insert","lines":["G"]},{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["O"]}],[{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["R"],"id":492},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["Y"]}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "],"id":493}],[{"start":{"row":41,"column":10},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":494}],[{"start":{"row":46,"column":41},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":495},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":8},"action":"insert","lines":["    "],"id":496}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":12},"action":"insert","lines":["    "],"id":497}],[{"start":{"row":47,"column":12},"end":{"row":47,"column":16},"action":"insert","lines":["    "],"id":498}],[{"start":{"row":47,"column":16},"end":{"row":47,"column":20},"action":"insert","lines":["    "],"id":499}],[{"start":{"row":47,"column":20},"end":{"row":47,"column":24},"action":"insert","lines":["    "],"id":500}],[{"start":{"row":47,"column":24},"end":{"row":47,"column":28},"action":"insert","lines":["    "],"id":501}],[{"start":{"row":46,"column":32},"end":{"row":46,"column":33},"action":"remove","lines":["s"],"id":502},{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"remove","lines":["k"]},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"remove","lines":["s"]},{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"remove","lines":["a"]},{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"remove","lines":["t"]}],[{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"insert","lines":["C"],"id":503},{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"insert","lines":["A"]},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"insert","lines":["T"]},{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"insert","lines":["E"]},{"start":{"row":46,"column":32},"end":{"row":46,"column":33},"action":"insert","lines":["G"]},{"start":{"row":46,"column":33},"end":{"row":46,"column":34},"action":"insert","lines":["O"]},{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"insert","lines":["R"]},{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"insert","lines":["Y"]}],[{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"remove","lines":["Y"],"id":504},{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"remove","lines":["R"]},{"start":{"row":46,"column":33},"end":{"row":46,"column":34},"action":"remove","lines":["O"]},{"start":{"row":46,"column":32},"end":{"row":46,"column":33},"action":"remove","lines":["G"]},{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"remove","lines":["E"]},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"remove","lines":["T"]},{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"remove","lines":["A"]},{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"remove","lines":["C"]}],[{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"insert","lines":["c"],"id":505},{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"insert","lines":["a"]},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"insert","lines":["t"]},{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"insert","lines":["e"]},{"start":{"row":46,"column":32},"end":{"row":46,"column":33},"action":"insert","lines":["g"]},{"start":{"row":46,"column":33},"end":{"row":46,"column":34},"action":"insert","lines":["o"]},{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"insert","lines":["r"]},{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"insert","lines":["y"]}],[{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"remove","lines":["s"],"id":506},{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"remove","lines":["k"]},{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"remove","lines":["s"]},{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"remove","lines":["a"]},{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"insert","lines":["c"],"id":507},{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"insert","lines":["a"]},{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"insert","lines":["t"]},{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"insert","lines":["e"]},{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"insert","lines":["g"]},{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"insert","lines":["o"]},{"start":{"row":47,"column":34},"end":{"row":47,"column":35},"action":"insert","lines":["r"]},{"start":{"row":47,"column":35},"end":{"row":47,"column":36},"action":"insert","lines":["y"]}],[{"start":{"row":47,"column":50},"end":{"row":47,"column":51},"action":"remove","lines":["s"],"id":508},{"start":{"row":47,"column":49},"end":{"row":47,"column":50},"action":"remove","lines":["k"]},{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"remove","lines":["s"]},{"start":{"row":47,"column":47},"end":{"row":47,"column":48},"action":"remove","lines":["a"]},{"start":{"row":47,"column":46},"end":{"row":47,"column":47},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":46},"end":{"row":47,"column":47},"action":"insert","lines":["c"],"id":509},{"start":{"row":47,"column":47},"end":{"row":47,"column":48},"action":"insert","lines":["a"]},{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"insert","lines":["t"]},{"start":{"row":47,"column":49},"end":{"row":47,"column":50},"action":"insert","lines":["e"]},{"start":{"row":47,"column":50},"end":{"row":47,"column":51},"action":"insert","lines":["g"]},{"start":{"row":47,"column":51},"end":{"row":47,"column":52},"action":"insert","lines":["o"]},{"start":{"row":47,"column":52},"end":{"row":47,"column":53},"action":"insert","lines":["r"]},{"start":{"row":47,"column":53},"end":{"row":47,"column":54},"action":"insert","lines":["y"]}],[{"start":{"row":50,"column":0},"end":{"row":53,"column":43},"action":"insert","lines":["# Function to fetch all our category in mongodb and pass it back to addTask.htmk <select> ","@app.route('/add_task')","def add_task():","    return render_template('addTask.html', "],"id":510}],[{"start":{"row":55,"column":4},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":511},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":50,"column":74},"end":{"row":50,"column":75},"action":"remove","lines":["k"],"id":512},{"start":{"row":50,"column":73},"end":{"row":50,"column":74},"action":"remove","lines":["s"]},{"start":{"row":50,"column":72},"end":{"row":50,"column":73},"action":"remove","lines":["a"]},{"start":{"row":50,"column":71},"end":{"row":50,"column":72},"action":"remove","lines":["T"]}],[{"start":{"row":50,"column":71},"end":{"row":50,"column":72},"action":"insert","lines":["C"],"id":513},{"start":{"row":50,"column":72},"end":{"row":50,"column":73},"action":"insert","lines":["a"]},{"start":{"row":50,"column":73},"end":{"row":50,"column":74},"action":"insert","lines":["t"]}],[{"start":{"row":50,"column":74},"end":{"row":50,"column":75},"action":"insert","lines":["e"],"id":514}],[{"start":{"row":50,"column":75},"end":{"row":50,"column":76},"action":"insert","lines":["g"],"id":515},{"start":{"row":50,"column":76},"end":{"row":50,"column":77},"action":"insert","lines":["o"]},{"start":{"row":50,"column":77},"end":{"row":50,"column":78},"action":"insert","lines":["r"]},{"start":{"row":50,"column":78},"end":{"row":50,"column":79},"action":"insert","lines":["y"]}],[{"start":{"row":50,"column":83},"end":{"row":50,"column":84},"action":"remove","lines":["k"],"id":516}],[{"start":{"row":50,"column":83},"end":{"row":50,"column":84},"action":"insert","lines":["l"],"id":517}],[{"start":{"row":25,"column":79},"end":{"row":25,"column":80},"action":"remove","lines":["k"],"id":518}],[{"start":{"row":25,"column":79},"end":{"row":25,"column":80},"action":"insert","lines":["l"],"id":519}],[{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"remove","lines":["k"],"id":520},{"start":{"row":51,"column":19},"end":{"row":51,"column":20},"action":"remove","lines":["s"]},{"start":{"row":51,"column":18},"end":{"row":51,"column":19},"action":"remove","lines":["a"]},{"start":{"row":51,"column":17},"end":{"row":51,"column":18},"action":"remove","lines":["t"]}],[{"start":{"row":51,"column":17},"end":{"row":51,"column":18},"action":"insert","lines":["c"],"id":521},{"start":{"row":51,"column":18},"end":{"row":51,"column":19},"action":"insert","lines":["a"]},{"start":{"row":51,"column":19},"end":{"row":51,"column":20},"action":"insert","lines":["t"]},{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"insert","lines":["e"]},{"start":{"row":51,"column":21},"end":{"row":51,"column":22},"action":"insert","lines":["g"]},{"start":{"row":51,"column":22},"end":{"row":51,"column":23},"action":"insert","lines":["o"]},{"start":{"row":51,"column":23},"end":{"row":51,"column":24},"action":"insert","lines":["r"]},{"start":{"row":51,"column":24},"end":{"row":51,"column":25},"action":"insert","lines":["y"]}],[{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"remove","lines":["k"],"id":522},{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"remove","lines":["s"]},{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"remove","lines":["a"]},{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"insert","lines":["c"],"id":523},{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"insert","lines":["a"]},{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"insert","lines":["t"]},{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"insert","lines":["e"]},{"start":{"row":52,"column":12},"end":{"row":52,"column":13},"action":"insert","lines":["g"]},{"start":{"row":52,"column":13},"end":{"row":52,"column":14},"action":"insert","lines":["o"]},{"start":{"row":52,"column":14},"end":{"row":52,"column":15},"action":"insert","lines":["r"]},{"start":{"row":52,"column":15},"end":{"row":52,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":53,"column":41},"end":{"row":53,"column":42},"action":"remove","lines":[","],"id":524}],[{"start":{"row":53,"column":41},"end":{"row":53,"column":42},"action":"insert","lines":[")"],"id":525}],[{"start":{"row":53,"column":34},"end":{"row":53,"column":35},"action":"remove","lines":["k"],"id":526},{"start":{"row":53,"column":33},"end":{"row":53,"column":34},"action":"remove","lines":["s"]},{"start":{"row":53,"column":32},"end":{"row":53,"column":33},"action":"remove","lines":["a"]},{"start":{"row":53,"column":31},"end":{"row":53,"column":32},"action":"remove","lines":["T"]}],[{"start":{"row":53,"column":31},"end":{"row":53,"column":32},"action":"insert","lines":["C"],"id":527},{"start":{"row":53,"column":32},"end":{"row":53,"column":33},"action":"insert","lines":["a"]},{"start":{"row":53,"column":33},"end":{"row":53,"column":34},"action":"insert","lines":["t"]},{"start":{"row":53,"column":34},"end":{"row":53,"column":35},"action":"insert","lines":["e"]},{"start":{"row":53,"column":35},"end":{"row":53,"column":36},"action":"insert","lines":["g"]},{"start":{"row":53,"column":36},"end":{"row":53,"column":37},"action":"insert","lines":["o"]},{"start":{"row":53,"column":37},"end":{"row":53,"column":38},"action":"insert","lines":["r"]},{"start":{"row":53,"column":38},"end":{"row":53,"column":39},"action":"insert","lines":["y"]}]]},"ace":{"folds":[],"scrolltop":279.6875,"scrollleft":0,"selection":{"start":{"row":58,"column":26},"end":{"row":58,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572329125353,"hash":"2de6bed198697a415146fd9b7958e58e0b86ff73"}