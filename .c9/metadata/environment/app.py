{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"insert","lines":[" "],"id":293},{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["o"]}],[{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"remove","lines":["o"],"id":294},{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"remove","lines":[" "]}],[{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"insert","lines":[" "],"id":295},{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["y"]}],[{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"remove","lines":["y"],"id":296}],[{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["t"],"id":297},{"start":{"row":19,"column":68},"end":{"row":19,"column":69},"action":"insert","lines":["o"]}],[{"start":{"row":22,"column":77},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":298},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":299}],[{"start":{"row":25,"column":0},"end":{"row":29,"column":41},"action":"insert","lines":["@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))"],"id":300}],[{"start":{"row":24,"column":1},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":301},{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["t"],"id":302},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"insert","lines":["h"]}],[{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"insert","lines":["i"],"id":303},{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"remove","lines":["s"],"id":304},{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"remove","lines":["i"]},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"remove","lines":["h"]},{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"remove","lines":["t"]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["w"],"id":305},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"insert","lines":["h"]},{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"insert","lines":["e"]},{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":[" "],"id":306},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["w"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":[" "],"id":307},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["c"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["l"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["i"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["c"]}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["k"],"id":308}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":[" "],"id":309}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["<"],"id":310},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":[">"]}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["a"],"id":311},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["t"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["t"],"id":312},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["t"]}],[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["d"],"id":313},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":[" "],"id":314},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["t"]},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["a"]},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["s"]},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["k"]}],[{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"insert","lines":[" "],"id":315}],[{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"remove","lines":[" "],"id":316}],[{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"insert","lines":[" "],"id":317},{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["b"]}],[{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["u"],"id":318},{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["t"]},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["t"]},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["o"]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["m"]}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"remove","lines":["m"],"id":319}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["n"],"id":320},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":[","]}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":[" "],"id":321},{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"remove","lines":["t"],"id":322}],[{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["h"],"id":323},{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"insert","lines":["i"]},{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":[" "],"id":324}],[{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"remove","lines":[" "],"id":325},{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"remove","lines":["s"]},{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"remove","lines":["i"]},{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"remove","lines":["h"]},{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"remove","lines":[" "]},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"remove","lines":[","]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"remove","lines":["n"]},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"remove","lines":["o"]},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"remove","lines":["t"]},{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"remove","lines":["t"]},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"remove","lines":["u"]},{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"remove","lines":["b"]},{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"remove","lines":[" "]},{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"remove","lines":[">"]},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"remove","lines":["k"]},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"remove","lines":["s"]},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"remove","lines":["a"]},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"remove","lines":["t"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"remove","lines":[" "]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["d"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["d"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["a"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"remove","lines":["<"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"remove","lines":[" "]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["k"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"remove","lines":["c"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"remove","lines":["i"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"remove","lines":["l"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"remove","lines":["c"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":[" "]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["e"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["w"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"remove","lines":["n"],"id":326},{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"remove","lines":["e"]},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"remove","lines":["h"]},{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"remove","lines":["w"]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["t"],"id":327},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"insert","lines":["h"]},{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"insert","lines":["i"]},{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":[" "],"id":328},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["f"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["u"]}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["n"],"id":329},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["c"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["t"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["i"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["o"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["n"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["w"]}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"remove","lines":["w"],"id":330}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":[" "],"id":331},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["w"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["i"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["l"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["l"]}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":[" "],"id":332},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["p"]},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["o"]},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["s"]},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"insert","lines":[" "],"id":333},{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"insert","lines":["n"]},{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["e"]},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["w"]}],[{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":[" "],"id":334},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["f"]}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"remove","lines":["f"],"id":335}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["d"],"id":336},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["a"]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["a"]}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"remove","lines":["a"],"id":337}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["t"],"id":338},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["a"]}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":[" "],"id":339},{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["t"]},{"start":{"row":25,"column":34},"end":{"row":25,"column":35},"action":"insert","lines":["o"]}],[{"start":{"row":25,"column":35},"end":{"row":25,"column":36},"action":"insert","lines":[" "],"id":340},{"start":{"row":25,"column":36},"end":{"row":25,"column":37},"action":"insert","lines":["m"]},{"start":{"row":25,"column":37},"end":{"row":25,"column":38},"action":"insert","lines":["o"]},{"start":{"row":25,"column":38},"end":{"row":25,"column":39},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":39},"end":{"row":25,"column":40},"action":"insert","lines":["d"],"id":341},{"start":{"row":25,"column":40},"end":{"row":25,"column":41},"action":"insert","lines":["o"]},{"start":{"row":25,"column":41},"end":{"row":25,"column":42},"action":"insert","lines":["d"]},{"start":{"row":25,"column":42},"end":{"row":25,"column":43},"action":"insert","lines":["b"]}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":[" "],"id":342},{"start":{"row":25,"column":44},"end":{"row":25,"column":45},"action":"insert","lines":["w"]},{"start":{"row":25,"column":45},"end":{"row":25,"column":46},"action":"insert","lines":["h"]},{"start":{"row":25,"column":46},"end":{"row":25,"column":47},"action":"insert","lines":["e"]},{"start":{"row":25,"column":47},"end":{"row":25,"column":48},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":48},"end":{"row":25,"column":49},"action":"insert","lines":[" "],"id":343},{"start":{"row":25,"column":49},"end":{"row":25,"column":50},"action":"insert","lines":["c"]},{"start":{"row":25,"column":50},"end":{"row":25,"column":51},"action":"insert","lines":["l"]},{"start":{"row":25,"column":51},"end":{"row":25,"column":52},"action":"insert","lines":["i"]},{"start":{"row":25,"column":52},"end":{"row":25,"column":53},"action":"insert","lines":["c"]},{"start":{"row":25,"column":53},"end":{"row":25,"column":54},"action":"insert","lines":["k"]}],[{"start":{"row":25,"column":54},"end":{"row":25,"column":55},"action":"insert","lines":[" "],"id":344},{"start":{"row":25,"column":55},"end":{"row":25,"column":56},"action":"insert","lines":["o"]},{"start":{"row":25,"column":56},"end":{"row":25,"column":57},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":57},"end":{"row":25,"column":58},"action":"insert","lines":[" "],"id":345},{"start":{"row":25,"column":58},"end":{"row":25,"column":59},"action":"insert","lines":["t"]},{"start":{"row":25,"column":59},"end":{"row":25,"column":60},"action":"insert","lines":["h"]},{"start":{"row":25,"column":60},"end":{"row":25,"column":61},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":61},"end":{"row":25,"column":62},"action":"insert","lines":[" "],"id":346},{"start":{"row":25,"column":62},"end":{"row":25,"column":63},"action":"insert","lines":["s"]},{"start":{"row":25,"column":63},"end":{"row":25,"column":64},"action":"insert","lines":["u"]},{"start":{"row":25,"column":64},"end":{"row":25,"column":65},"action":"insert","lines":["m"]}],[{"start":{"row":25,"column":64},"end":{"row":25,"column":65},"action":"remove","lines":["m"],"id":347}],[{"start":{"row":25,"column":64},"end":{"row":25,"column":65},"action":"insert","lines":["b"],"id":348},{"start":{"row":25,"column":65},"end":{"row":25,"column":66},"action":"insert","lines":["m"]},{"start":{"row":25,"column":66},"end":{"row":25,"column":67},"action":"insert","lines":["i"]},{"start":{"row":25,"column":67},"end":{"row":25,"column":68},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":68},"end":{"row":25,"column":69},"action":"insert","lines":[" "],"id":349},{"start":{"row":25,"column":69},"end":{"row":25,"column":70},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":69},"end":{"row":25,"column":70},"action":"remove","lines":["s"],"id":350}],[{"start":{"row":25,"column":69},"end":{"row":25,"column":70},"action":"insert","lines":["b"],"id":351},{"start":{"row":25,"column":70},"end":{"row":25,"column":71},"action":"insert","lines":["u"]},{"start":{"row":25,"column":71},"end":{"row":25,"column":72},"action":"insert","lines":["t"]},{"start":{"row":25,"column":72},"end":{"row":25,"column":73},"action":"insert","lines":["t"]},{"start":{"row":25,"column":73},"end":{"row":25,"column":74},"action":"insert","lines":["o"]},{"start":{"row":25,"column":74},"end":{"row":25,"column":75},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":75},"end":{"row":25,"column":76},"action":"insert","lines":[" "],"id":352},{"start":{"row":25,"column":76},"end":{"row":25,"column":77},"action":"insert","lines":["i"]},{"start":{"row":25,"column":77},"end":{"row":25,"column":78},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":78},"end":{"row":25,"column":79},"action":"insert","lines":[" "],"id":353},{"start":{"row":25,"column":79},"end":{"row":25,"column":80},"action":"insert","lines":["a"]},{"start":{"row":25,"column":80},"end":{"row":25,"column":81},"action":"insert","lines":["d"]},{"start":{"row":25,"column":81},"end":{"row":25,"column":82},"action":"insert","lines":["d"]}],[{"start":{"row":25,"column":82},"end":{"row":25,"column":83},"action":"insert","lines":["."],"id":354},{"start":{"row":25,"column":83},"end":{"row":25,"column":84},"action":"insert","lines":["t"]},{"start":{"row":25,"column":84},"end":{"row":25,"column":85},"action":"insert","lines":["a"]},{"start":{"row":25,"column":85},"end":{"row":25,"column":86},"action":"insert","lines":["s"]},{"start":{"row":25,"column":86},"end":{"row":25,"column":87},"action":"insert","lines":["l"]}],[{"start":{"row":25,"column":86},"end":{"row":25,"column":87},"action":"remove","lines":["l"],"id":355},{"start":{"row":25,"column":85},"end":{"row":25,"column":86},"action":"remove","lines":["s"]},{"start":{"row":25,"column":84},"end":{"row":25,"column":85},"action":"remove","lines":["a"]},{"start":{"row":25,"column":83},"end":{"row":25,"column":84},"action":"remove","lines":["t"]},{"start":{"row":25,"column":82},"end":{"row":25,"column":83},"action":"remove","lines":["."]}],[{"start":{"row":25,"column":82},"end":{"row":25,"column":83},"action":"insert","lines":["T"],"id":356},{"start":{"row":25,"column":83},"end":{"row":25,"column":84},"action":"insert","lines":["a"]},{"start":{"row":25,"column":84},"end":{"row":25,"column":85},"action":"insert","lines":["s"]},{"start":{"row":25,"column":85},"end":{"row":25,"column":86},"action":"insert","lines":["k"]},{"start":{"row":25,"column":86},"end":{"row":25,"column":87},"action":"insert","lines":["."]}],[{"start":{"row":25,"column":87},"end":{"row":25,"column":88},"action":"insert","lines":["h"],"id":357},{"start":{"row":25,"column":88},"end":{"row":25,"column":89},"action":"insert","lines":["t"]},{"start":{"row":25,"column":89},"end":{"row":25,"column":90},"action":"insert","lines":["m"]},{"start":{"row":25,"column":90},"end":{"row":25,"column":91},"action":"insert","lines":["l"]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "],"id":358}],[{"start":{"row":25,"column":93},"end":{"row":25,"column":94},"action":"insert","lines":["W"],"id":359},{"start":{"row":25,"column":94},"end":{"row":25,"column":95},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":94},"end":{"row":25,"column":95},"action":"remove","lines":["e"],"id":360},{"start":{"row":25,"column":93},"end":{"row":25,"column":94},"action":"remove","lines":["W"]},{"start":{"row":25,"column":92},"end":{"row":25,"column":93},"action":"remove","lines":["l"]},{"start":{"row":25,"column":91},"end":{"row":25,"column":92},"action":"remove","lines":["m"]},{"start":{"row":25,"column":90},"end":{"row":25,"column":91},"action":"remove","lines":["t"]},{"start":{"row":25,"column":89},"end":{"row":25,"column":90},"action":"remove","lines":["h"]},{"start":{"row":25,"column":88},"end":{"row":25,"column":89},"action":"remove","lines":["."]}],[{"start":{"row":25,"column":88},"end":{"row":25,"column":89},"action":"insert","lines":["."],"id":361},{"start":{"row":25,"column":89},"end":{"row":25,"column":90},"action":"insert","lines":["h"]},{"start":{"row":25,"column":90},"end":{"row":25,"column":91},"action":"insert","lines":["t"]},{"start":{"row":25,"column":91},"end":{"row":25,"column":92},"action":"insert","lines":["m"]},{"start":{"row":25,"column":92},"end":{"row":25,"column":93},"action":"insert","lines":["l"]}],[{"start":{"row":25,"column":93},"end":{"row":25,"column":94},"action":"insert","lines":["."],"id":362}],[{"start":{"row":25,"column":94},"end":{"row":25,"column":95},"action":"insert","lines":[" "],"id":363},{"start":{"row":25,"column":95},"end":{"row":25,"column":96},"action":"insert","lines":["W"]},{"start":{"row":25,"column":96},"end":{"row":25,"column":97},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":97},"end":{"row":25,"column":98},"action":"insert","lines":[" "],"id":364},{"start":{"row":25,"column":98},"end":{"row":25,"column":99},"action":"insert","lines":["c"]},{"start":{"row":25,"column":99},"end":{"row":25,"column":100},"action":"insert","lines":["o"]},{"start":{"row":25,"column":100},"end":{"row":25,"column":101},"action":"insert","lines":["n"]},{"start":{"row":25,"column":101},"end":{"row":25,"column":102},"action":"insert","lines":["v"]},{"start":{"row":25,"column":102},"end":{"row":25,"column":103},"action":"insert","lines":["e"]},{"start":{"row":25,"column":103},"end":{"row":25,"column":104},"action":"insert","lines":["r"]},{"start":{"row":25,"column":104},"end":{"row":25,"column":105},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":105},"end":{"row":25,"column":106},"action":"insert","lines":[" "],"id":365},{"start":{"row":25,"column":106},"end":{"row":25,"column":107},"action":"insert","lines":["t"]},{"start":{"row":25,"column":107},"end":{"row":25,"column":108},"action":"insert","lines":["h"]},{"start":{"row":25,"column":108},"end":{"row":25,"column":109},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":109},"end":{"row":25,"column":110},"action":"insert","lines":[" "],"id":366},{"start":{"row":25,"column":110},"end":{"row":25,"column":111},"action":"insert","lines":["f"]},{"start":{"row":25,"column":111},"end":{"row":25,"column":112},"action":"insert","lines":["o"]},{"start":{"row":25,"column":112},"end":{"row":25,"column":113},"action":"insert","lines":["r"]},{"start":{"row":25,"column":113},"end":{"row":25,"column":114},"action":"insert","lines":["n"]},{"start":{"row":25,"column":114},"end":{"row":25,"column":115},"action":"insert","lines":["m"]}],[{"start":{"row":25,"column":115},"end":{"row":25,"column":116},"action":"insert","lines":[" "],"id":367}],[{"start":{"row":25,"column":115},"end":{"row":25,"column":116},"action":"remove","lines":[" "],"id":368},{"start":{"row":25,"column":114},"end":{"row":25,"column":115},"action":"remove","lines":["m"]},{"start":{"row":25,"column":113},"end":{"row":25,"column":114},"action":"remove","lines":["n"]}],[{"start":{"row":25,"column":113},"end":{"row":25,"column":114},"action":"insert","lines":["m"],"id":369}],[{"start":{"row":25,"column":114},"end":{"row":25,"column":115},"action":"insert","lines":[" "],"id":370},{"start":{"row":25,"column":115},"end":{"row":25,"column":116},"action":"insert","lines":["t"]},{"start":{"row":25,"column":116},"end":{"row":25,"column":117},"action":"insert","lines":["o"]}],[{"start":{"row":25,"column":117},"end":{"row":25,"column":118},"action":"insert","lines":[" "],"id":371},{"start":{"row":25,"column":118},"end":{"row":25,"column":119},"action":"insert","lines":["d"]},{"start":{"row":25,"column":119},"end":{"row":25,"column":120},"action":"insert","lines":["i"]},{"start":{"row":25,"column":120},"end":{"row":25,"column":121},"action":"insert","lines":["c"]},{"start":{"row":25,"column":121},"end":{"row":25,"column":122},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":122},"end":{"row":25,"column":123},"action":"insert","lines":["i"],"id":372},{"start":{"row":25,"column":123},"end":{"row":25,"column":124},"action":"insert","lines":["o"]},{"start":{"row":25,"column":124},"end":{"row":25,"column":125},"action":"insert","lines":["n"]},{"start":{"row":25,"column":125},"end":{"row":25,"column":126},"action":"insert","lines":["r"]}],[{"start":{"row":25,"column":125},"end":{"row":25,"column":126},"action":"remove","lines":["r"],"id":373}],[{"start":{"row":25,"column":125},"end":{"row":25,"column":126},"action":"insert","lines":["r"],"id":374},{"start":{"row":25,"column":126},"end":{"row":25,"column":127},"action":"insert","lines":["y"]}],[{"start":{"row":25,"column":126},"end":{"row":25,"column":127},"action":"remove","lines":["y"],"id":375},{"start":{"row":25,"column":125},"end":{"row":25,"column":126},"action":"remove","lines":["r"]}],[{"start":{"row":25,"column":125},"end":{"row":25,"column":126},"action":"insert","lines":["a"],"id":376},{"start":{"row":25,"column":126},"end":{"row":25,"column":127},"action":"insert","lines":["r"]},{"start":{"row":25,"column":127},"end":{"row":25,"column":128},"action":"insert","lines":["y"]}],[{"start":{"row":25,"column":128},"end":{"row":25,"column":129},"action":"insert","lines":[" "],"id":377},{"start":{"row":25,"column":129},"end":{"row":25,"column":130},"action":"insert","lines":["s"]},{"start":{"row":25,"column":130},"end":{"row":25,"column":131},"action":"insert","lines":["o"]}],[{"start":{"row":25,"column":131},"end":{"row":25,"column":132},"action":"insert","lines":[" "],"id":378}],[{"start":{"row":25,"column":132},"end":{"row":25,"column":133},"action":"insert","lines":["c"],"id":379}],[{"start":{"row":25,"column":132},"end":{"row":25,"column":133},"action":"remove","lines":["c"],"id":380}],[{"start":{"row":25,"column":132},"end":{"row":25,"column":133},"action":"insert","lines":["c"],"id":381},{"start":{"row":25,"column":133},"end":{"row":25,"column":134},"action":"insert","lines":["a"]},{"start":{"row":25,"column":134},"end":{"row":25,"column":135},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":135},"end":{"row":25,"column":136},"action":"insert","lines":[" "],"id":382},{"start":{"row":25,"column":136},"end":{"row":25,"column":137},"action":"insert","lines":["b"]},{"start":{"row":25,"column":137},"end":{"row":25,"column":138},"action":"insert","lines":["e"]}],[{"start":{"row":25,"column":138},"end":{"row":25,"column":139},"action":"insert","lines":[" "],"id":383},{"start":{"row":25,"column":139},"end":{"row":25,"column":140},"action":"insert","lines":["u"]},{"start":{"row":25,"column":140},"end":{"row":25,"column":141},"action":"insert","lines":["n"]},{"start":{"row":25,"column":141},"end":{"row":25,"column":142},"action":"insert","lines":["d"]},{"start":{"row":25,"column":142},"end":{"row":25,"column":143},"action":"insert","lines":["e"]},{"start":{"row":25,"column":143},"end":{"row":25,"column":144},"action":"insert","lines":["r"]},{"start":{"row":25,"column":144},"end":{"row":25,"column":145},"action":"insert","lines":["s"]},{"start":{"row":25,"column":145},"end":{"row":25,"column":146},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":146},"end":{"row":25,"column":147},"action":"insert","lines":["o"],"id":384},{"start":{"row":25,"column":147},"end":{"row":25,"column":148},"action":"insert","lines":["d"]},{"start":{"row":25,"column":148},"end":{"row":25,"column":149},"action":"insert","lines":["d"]}],[{"start":{"row":25,"column":148},"end":{"row":25,"column":149},"action":"remove","lines":["d"],"id":385},{"start":{"row":25,"column":147},"end":{"row":25,"column":148},"action":"remove","lines":["d"]}],[{"start":{"row":25,"column":147},"end":{"row":25,"column":148},"action":"insert","lines":["d"],"id":386}],[{"start":{"row":25,"column":147},"end":{"row":25,"column":148},"action":"remove","lines":["d"],"id":387}],[{"start":{"row":25,"column":147},"end":{"row":25,"column":148},"action":"insert","lines":["o"],"id":388},{"start":{"row":25,"column":148},"end":{"row":25,"column":149},"action":"insert","lines":["d"]}],[{"start":{"row":25,"column":149},"end":{"row":25,"column":150},"action":"insert","lines":[" "],"id":389},{"start":{"row":25,"column":150},"end":{"row":25,"column":151},"action":"insert","lines":["b"]},{"start":{"row":25,"column":151},"end":{"row":25,"column":152},"action":"insert","lines":["y"]}],[{"start":{"row":25,"column":152},"end":{"row":25,"column":153},"action":"insert","lines":[" "],"id":390}],[{"start":{"row":25,"column":153},"end":{"row":25,"column":154},"action":"insert","lines":["m"],"id":391},{"start":{"row":25,"column":154},"end":{"row":25,"column":155},"action":"insert","lines":["o"]},{"start":{"row":25,"column":155},"end":{"row":25,"column":156},"action":"insert","lines":["n"]},{"start":{"row":25,"column":156},"end":{"row":25,"column":157},"action":"insert","lines":["d"]},{"start":{"row":25,"column":157},"end":{"row":25,"column":158},"action":"insert","lines":["o"]}],[{"start":{"row":25,"column":157},"end":{"row":25,"column":158},"action":"remove","lines":["o"],"id":392},{"start":{"row":25,"column":156},"end":{"row":25,"column":157},"action":"remove","lines":["d"]}],[{"start":{"row":25,"column":156},"end":{"row":25,"column":157},"action":"insert","lines":["g"],"id":393},{"start":{"row":25,"column":157},"end":{"row":25,"column":158},"action":"insert","lines":["o"]},{"start":{"row":25,"column":158},"end":{"row":25,"column":159},"action":"insert","lines":["."]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":25,"column":159},"end":{"row":25,"column":159},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572175839685,"hash":"d1bb67de92fcabee0910c97d57868bbbd49c8f28"}