karger_runtime = [
    19731500.0,
13376875.0,
16147958.0,
14371708.0,
240299292.0,
268284333.0,
209742375.0,
239537417.0,
1702043500.0,
1672645375.0,
1632752583.0,
1745592041.0,
7335973584.0,
7252139917.0,
8085440125.0,
7656908750.0,
9986602709.0,
11523634791.0,
10379119500.0,
11141554583.0,
22060607625.0,
22095292083.0,
20530139000.0,
23142845042.0,
56754153541.0,
58565779750.0,
58420352958.0,
58873094708.0,
134010095875.0,
128170110584.0,
130211527959.0,
129439174667.0,
257588841916.0,
258635898625.0,
260853956583.0,
258256822417.0,
320220283417.0,
321425372667.0,
313480846125.0,
325431798916.0,
609190989791.0,
608415688208.0,
609426155250.0,
570206744708.0,
706357488875.0,
697943213125.0,
690077010834.0,
745998881250.0,
1269611420000.0,
1269493672041.0,
1269306493833.0,
1266458447958.0,
1414460136417.0,
1442772754209.0,
1424607655666.0,
1414643955875.0,
]

karger_discovery = [
    3455625.0,
2236791.0,
2744167.0,
2458000.0,
26685125.0,
25370541.0,
23177375.0,
26222166.0,
123374125.0,
122105125.0,
112541000.0,
121486625.0,
417247917.0,
419687375.0,
475616042.0,
448064625.0,
487682041.0,
571469458.0,
516143041.0,
549510375.0,
1011022000.0,
992045708.0,
934360500.0,
1053217167.0,
2180048208.0,
2236631917.0,
2238050458.0,
2266980834.0,
4581623083.0,
4416449042.0,
4524823375.0,
4471847000.0,
8335967125.0,
8259039417.0,
8337357959.0,
8326649167.0,
9707610041.0,
9736197084.0,
9455485041.0,
9850405958.0,
17407820000.0,
17354319500.0,
17421415166.0,
16167959667.0,
19295337125.0,
19363343417.0,
19149139583.0,
20649293333.0,
33984272792.0,
33449564250.0,
33411557542.0,
33290094291.0,
36269376000.0,
37275865542.0,
36480520625.0,
36087676583.0,
]

stoer_runtime = [
    952462.1,
846419.5,
858611.1,
849654.7,
3712249.9,
3830532.4,
3867437.4,
3926768.6,
21717925.0,
17700328.9,
18178249.6,
16766661.1,
41794298.4,
39147987.5,
39929497.3,
39356217.2,
71717298.0,
72112665.9,
72417504.2,
73447162.1,
113991215.4,
111091987.0,
109228050.3,
114574063.3,
271632782.9,
279370483.4,
271227243.4,
270195222.0,
511061055.2,
497905751.3,
511434195.9,
524118735.9,
765539229.8,
807738372.7,
823449401.6,
809751784.9,
1218479947.1,
1220514181.0,
1269579718.5,
1284392067.5,
1721640794.0,
1739136142.9,
1669194686.7,
1676883716.6,
2252189298.4,
2162349111.0,
2174460290.1,
2225443714.6,
2786941672.5,
2862204300.2,
2803237450.7,
2810171203.7,
3678713264.3,
3628896640.5,
3663261322.0,
3637159119.5,]

import matplotlib.pyplot as plt
from graph.graph import read_all

mincut_graphs = read_all("/Users/dilettarigo/Desktop/advanced-algorithms/assignment-3/mincut_dataset", 56)

x = [g.get_n() for g in mincut_graphs]

plt.plot(x, karger_runtime, label="Karger-Stein's runtime")
plt.plot(x, karger_discovery, label="Karger-Stein's discovery time")
plt.plot(x, stoer_runtime, label="Stoer-Wagner's runtime")

plt.title("Comparison of the two algorithms")
plt.xlabel("n")
plt.ylabel("Time")
plt.legend()
plt.show()
