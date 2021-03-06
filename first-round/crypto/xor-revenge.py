# Repeated key xor
# Tìm hiểu thêm tại đây: https://en.wikipedia.org/wiki/XOR_cipher#Example
original_message = "a447dba48276ce3c7b41ce28dbc5c2df1764c8f08a3c5ceccb592e0070b03dea8146d3ef866585297b50c128d8c496971a729be38e3e49f7dc0a764f36b42bedc859c1aa9466873174518b28f9d092c311659bbfcb244d89cd426d5571bd2ca8c87cdcaa893ece09725b856cd3d5c2c316769cb39c235ae7995a6d5036bc36f28708d9b6c77a8b3f7e1d8540df9191d41f7986f68f6c5cebdc43700070b43be39b0494bb867987307d02cc669ad483d4161d8deb9b3e4df0ca436d4e3af532f38c4fdda180329a367f4f8b28f5df87971c7891b4986c4dfadc592e0070b939f48d4c94b88e66867e7243d17adfd5ce970d6387e39b294ca3d1436f0075ba34e2c608fcaac77e81317147c128c9dee8d610709aeac76c7cebd647635336a237f3844cdae89332863f6c47856adfd48c970d629ae399255be6dd0a6b4636a130e3c843ddabc7718f337f02c47c9ad98bda5e6081e7836c49a3d2446b4673fb78ce8d08dcae83328c327b41ce28d2d08bc5521d89fd8f6c5febdc4422547eb021a68549d0aac777973b3a41ca66ced081c352379cfb8e6c4aecc00a714879ba33a68041c7ef8f778f3a3a43cb6c9ac597c510728cb38a3b49fa950a75417abe31e88f08c0a090739c3a3a43856fc8d483c4071d81e1842208f3d646670061bc2ceec84994b8887d8a3b7402c76dd4d28a97107290e7cb3847a3d05e2c0057f535f3845cddac887e812c7f46856ed6d08597166286f4cb2041eec9467b0077a178f2804d94bb8862ce317c02d160df9192d81272c4b3852322f4d044660062ba78f48d5ed1ae8b32872a6902d569cec587c51039e2c0832d43e6d70622747eba35e79b08c7bb86608b3a3a43d128ced987971c7891b4986c4ae2da41225578a131eac840d1ef93679c307f468569d4d5c2c3117883b38a6c5be6d85e2c0042bd37eb895b94be927b8d35765b8564d5de89d21a1d89e48a350689ea5f664473bb34ffc85cdcaac77e8b3f7e47d728d5d7c2c31672c8f499235df39907225073a730e7985b94a78232993f6902d66dccd48cc31b7286b3c66c5cecd641224136a62ce39808d2a095658f2c7e0c8540df9195d80c72e2fd843e45e2d50a614c79a130e39b1294ad8b738d353a76887bd2d890c3523782f68a225baf995e674e78bc2ba69b40dbaa943ece3f3a46cc6fd3c583db5e6089e7882406a3ff45700065ba35e3c85ad1ae947d807e6e4ac028d9dd8dc3167e86f4cb244df1dc20715564a52aef9b4dd0efb37a81337b519e28d3c5c2c41b7285f68f6c44ead24f224560b02aff8746d1ef947a812b7646856adf9195d21f6581fd8c6c5becd44f76487fbb3fa68547c6aac77f8b307b41cc66dd91cf97127e83f6e13c5aeaca456c0071b42ae4c608e0a782328a3f6849887bd1d88cd91b73c8f1843508ebd84e22537eba2af2c54bc6a097628b3a3a4ac461c89dc2df1764c8f58a2f4da3da46674178f52bee895ed1a1c932ac2b6e02ca7cd2d490970a7f89fdcb3840e6b35a67527bb436e3865c94bc847d99323602d160dfc3879709769bb385235cebd044650065b639f49108d5ad88679a7e724bc828dbc5c2d6127bc699c9055ca4ca0a63007aba36e1c85bc0a0956bc27e694ac466d19dc0970a7f8db3892351a3ca4b6b4438f57ad6814dd7aac770977e6a4bc06bdf9dc2ce1162cfff876c44e6d8586c003bf511a1844494ad82329a3f714bcb2f9ac88dc25e7886b39f244d89ed45775236a137eb875ac6a0903cce0a734ec928ced987d95e39c6bdcb265df0cd0a664f78f22ca68a5ad1ae8c328f306356cd61d4d6cc955e5f8db3832944e7994b224877bb3ca6875dc0e1c730a03f7747827b9af08ed50739cab3a32922f4d843764572f978e5844dd5bd8b6bce297b4cd161d4d6c2c311379bfb8a274da3d14b6c4465fb52d28047d9ae94329c3b7c57d66dde9fc2e4117a8db382225bf7d044615436a137e98308dbb98260ce3673518569d9c58bd81064c8f2852808f4d05e6a4f63a178f58951dda180328f306356cd61d4d6c2df1b379ce699224de7994b75416fdf3ef48745948e8b70977e7b4cc128cdd08edc1b73c8e7846c49a3d74f635274ac78f29a4dd1e3c765863b68478560df9192db116798f68f6c4cecce44225479f52bef9c08c3a6937ace367351856adbd289971f7089fa853f5ca3cd42672a64ba2de18008d6ae9579c07e4a43cb61d99191c01b7b84f68f6c41edca43664536bd31ebc847daac82328f397b4bcb249ad08eda11649cb39f2347a3d45f614836a137a68a4dd5bdc932ac2b6e02cd6d9ac58dd8153789b38f294df3b348704577a130a68946d0ef817d9c3d7f468560d3dc91d21271c8e7846c5cf1c00a764f36b43be58d58c0ef937a8b7e694bd17ddbc58bd81039c8d99e3f5ca3de4522577fa130a6815c98ef8f77ce2a724dd06fd2c5cc9727789db39c2346a4cd0a644971a02ae3e247c1bbc77380276e4acc66dd918bd15e6e87e6cb2b41f5dc0a6b4e36a137a68e4dd5bdc918cc0a7247cb28ced48edb5e7a8dbfc96c7cebd647635336b639ea844dd0ef88679a723a51d17acfd685db17798fb39f2308e8dc4f72007ebc2ba69e47ddac82328b287f4c8b2898e587db123785f6cb3840e699466d4e71f52bf2875acde1c518af32785b856fd6d08cd41b73c8f29f6c5cebdc0a64527fb036e29b08d7a388618b2d6e02d1679ad98bda52379afc872041edde0a6a4965f53dff8d5b98ef867c8a7e4e4aca65dbc2c2c40a628cfa8e2808f7d14f224364ba2fe2c849d3ae8e7cc054524bd628d5c38bd0177989ffcb295bf7d047635473f530e78c08d6aa827cce3d764dd66d9a9cc2c316729af6cb3b4df1dc0a725279b739e4845194a98e749a273a56ca28c9d89ac3073787f5cb3840e6d406225277bb3fef864f94a9957d8354784ddc7b9ad88c970a7f8dfa996c45eadd5e674578a678f28708cda0927c897e7b46d064cec2c2db177c8db3aa204afa950a754879f52be38d45d1abc766817e78478567d4d4c2d818379cfb8e6c47efdd4f715438f519f2c85cdcae931883317747cb7c9691b6df117a89e0cb3e4de2d543784572f52fef9c4094aec761873d7147cb61d4d6c2db0b658bfbcb3840e2cd0a6a4536bd39e2c846dbef8e768b3f3a4aca7f9ade8ed35e7f8db39c2d5bad99626b5336bd3de79a5c94bc867c85547b56857cd2d4c2c316789df4833808ae9942670061b42ba69b4794a388619a7e7247856cd3d58c900a378de58e2208e8d74575007ebc2ba6875fdaef86758b703a61f14ec1ff8dc3535c8deac61e4df6ca4f660d54a02cabd95cc7e2937add736916c86dc7bbc0e41b6581fc9e3f44fa9508224873f52be7814c98ef807b98377445857dca918dd95e6380f6cb3f40ecce0a6d4636b637f39a49d3aac932cc097247d76d9ad08f973728ca99aa204afa995d634c7db03ca6875ed1bdc766817e724bc828dbdf86970d769cb38f235fed9949704f65a675ea8d4fd3aa8329ce2a7247856bc8de95d35e788eb3892351f0994c6d4c7aba2fe38c08d5a183329e3f7949c06c9ad88cbd1c7280fa852806a3f14f634465f528e99858d1abc7679e7e7247d76d9ad08cd35e6380f6992904a3d243665336b93de78641daa8c77b807e7f54c07ac39186de0c728be7822346a3cd45224773a178e7c84ad1bb93779c7e764dca6394bbc0fe183791fc9e6c49ead70d760065b639f48d4c98edc753823c6302d669d3d5ce975c6e87e6cb2d41ed9e5e224863b839e8c608f5ac93328f306302c161dcd787c51b799cb38a224ca3f00d660062bd2ae99f08cda0923281387c02d160df91a1db17718e9989294be2cc5967007fa17fe2c845d1ae893297316f05d76d9ad0c2c70d6e8bfb84620a899b7e6a45369634ef8e4e8bedc74686317743d628dbc289d21a3bc8f1872347e7994e70417fbb31e88f08d2bd887fce367351856edbd287997435bbfb9e2f43a3d05e2e02369434e49108c7ae8e76c27e6857c76ad3df8597167e9bb38e354df0970a20617fbb7ff2c846dbef9073977e6e4d857bced090c35e6380f6982908e0d644744564a639f28147dabccb3297316f02c26dce918fd2411dbff6cb2847ed9e5e224b7fb934a69b40d5a18c61ce327349c028c3de979716729af6c76c61a3c9586d4d7fa63da8c862c1bc93329a2c6302c466de9183c1117e8cb3892941edde0a69497ab93de2c408c7ba956487287f0e857fd2d096d208729abdc94660e6995a635565b03caac849daabc74686317743d628c8d483db176d8df7cb2441f0994c634373f535f39b5c93b9823299367356c066dfd5c2d2087286b386235ae6995d6a4578f530e3c840d1ae9576ce2a7243d128d6d091c3746789e19f6222a1f44b6c0c34f519ea8a5194bc867b8a723a56cd6dd49190d6103780fa986c40e2d74e710079a33df4c840ddbcc761863168568560dbd890971f64c8fb8e6c44e6cd0a6d5562f539a68447daa8c7618739720c852af39183de10309cb38c2347e7994b762a62bd31f5c80594b68867c92c7f02d160df9184de0c649cb3ac3e4de6d748674178f52bef864bd1efa97b8d353a55c47b9ada8bdb12728cbdc9467cebd647635331a678e3914dc7ef907b8a3b7447c1249ad08cd35e7686fc9f244df199486d5936a62ce39858d1abc7679e7e7b4cc128cadd83ce186284ff926c5befd85a724572f519ea8a5194ae8460812d6902d160df918ad21f73c699c91b49eacd0a644f64f52cee8d08d6a3887d8a273a76ca7dc89dc2f6127591bfc96c40e69959634972f978ee815b94b9887b8d3b3a56cd61d9dac2c0176380b38a2208ecdd4e224175b63de89c0694edac7b8a796902c267d4df839716769ef6cb2d22e1cc4d654978f278ee8d49c6bbc7739a2a7b41ce249adf8dc3167e86b4cb295ee6d70a604573bb78ee8d49c6abc76b8b2a34008540df9180d21063c8f7843b46a3d844660073ad2ce3864cd1abc77a872d3a4ac466de9196d809769af7e11840ecd44b710e36f716e7854d93bcc75c8b296e0e854fc8d487d91772c4b38a224ca3ce4f254436b434eac84ad1ef957b89366e02c660dfd490ce5e7e8eb3922d0fe7994c6d5271bc2ee3c847c1bdc779822b7449886ed5c3cfd50c7681fd984646e6ce0a6e4577b13df4c408dcaa9577c07c1076cd67d7d091970c7289f083294ca3d65f760077bb3ca69b40dba08c329a367f02c767c3969197167686f7cb6108ebdc0a714573b83de2c84994a38866ce307341c07a9ac58ad61037a9ff893506a3f74f755436a239f5c85cd5a38b779c546e4ac4669af08ed507379cfc846008e1cc5e224c79ba33e38c08c0a0c7708b7e7b02dc6ddbc3c2d80c379bfccb3547f6d74d675238f510ef9b08dcae8e60ce297b51856ad6de8cd35e7686f7cb2f5df799466d4e71f978e5895bd7ae837b8039104dd36dc8918ade0d37bcbe982441f1cd04227673bc36f5c85bc0ba8479ce316f568567dc918ade0d3785e6982f44e6dd0a63527ba6768cca78ddbf8232872a3602d660cfd2899a18768bf6c76e08c2d5487b0071a72de89c4dd0e3c7629b32764bcb6f9aff87c00a378cfc9c2208f7d60a714962f536e3905c94bb88328637770c852afbc5c2db1b769be7cb244da3da4b6c2a63bb3ce39a5bc0ae8976ce367b4ec328d7c8c2c011658ce0c56e08d7d14f704536a23df48d08d5ef8177997e6941c47cced490d21a3784f29e2b40f0950a634e72f52cee8d4694aa91779c27754cc028ddd096df1b658df7cb2e4debd044662a57b93affc849daabc75c8b296e0e8578dbd289de1070c8fa856c4df5dc4422547fb230f28d5a98ef9073872a734cc228cedec2df1b769ab39c2449f7995e6a456ff52be7814c9a"
test_key = "11111111111111111111111111111111"
test_mess = (
    "testasld;fjasldfjasldfsldfjasdlf"
    "j230523u509uas jvx.cvmnzxvxclvjq"
    "l234!#$^%@#$^@#$(^%*)%^&(*^&%*+_"
    "^&*)+}{:'}12dfgsdfg3qtsdgsdfgdsf"
)
test_result = (
    "4554424550425d550a575b50425d55575b50425d5557425d55575b5042555d57"
    "5b03020104030244040108445042115b47491f52475c5f4b494749525d475b40"
    "5d03020550425557504255570003025557505755504255575042555755425750"
    "4255574003504255575042555750425502465557504255575042555750425555"
)

KEY_LENGTH = 32


def encrypt(message: str, key: bytes) -> bytes:
    # chuyển string message thành byte
    byte_message = message.encode("utf-8")

    ciphertext = []
    # đi qua từng byte trong message
    for index in range(len(byte_message)):
        # nếu index vượt quá độ dài key, ta dùng lại key bắt đầu từ byte đầu tiên (từ đó có tên repeated key xor)
        current = byte_message[index] ^ key[index % len(key)]
        # if index % len(key) == 0:
        #     print(byte_message[index], current, chr(byte_message[index]), hex(current))
        ciphertext.append(current)
    return bytes(ciphertext)


# Có vẻ như 1 byte là không đủ an toàn, lần này mình sẽ dùng cả 32 bytes cho key
# key = test_key.encode("utf-8")
# message = test_mess
# ciphertext = encrypt(message, key)
# print(ciphertext.hex())
# print(len(key))


def prepare_result(cipher_mess):
    cipher_list = [cipher_mess[i : i + 2] for i in range(0, len(cipher_mess), 2)]
    cipher_dict = {}
    for index in range(KEY_LENGTH):
        cipher_dict[index] = []
    for index in range(len(cipher_list)):
        cipher_dict[index % KEY_LENGTH].append(cipher_list[index])
    return cipher_dict


def decrypt(byte_message, key):
    result = []
    for text in byte_message:
        current: int = int(text, 16) ^ key
        ans = chr(current)
        result.append(ans)
    final = "".join(result)
    return final


### TESTING
cipher_dict = prepare_result(original_message)

possible_value_dict = {}
for key_index in range(0, KEY_LENGTH):
    possible_value_dict[key_index] = []
    for key_byte in range(0, 256):  # ascii max value
        ans = decrypt(cipher_dict[key_index], key_byte)
        if ans is not None:
            possible_value_dict[key_index].append(ans)


def get_letter_count(text):
    LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    letter_count = {}
    for char_ in LETTERS:
        letter_count[char_] = 0

    for letter in text.upper():
        if letter in LETTERS:
            letter_count[letter] += 1
    return letter_count


def choose_based_on_freq_alphabet(possible_value_list):
    final_string = ""
    best_score = 0
    for string_ in possible_value_list:
        letter_freq = get_letter_count(string_)
        freq_letter_in_english = [
            letter_freq["E"],
            letter_freq["T"],
            letter_freq["A"],
            letter_freq["O"],
            letter_freq["I"],
            letter_freq["N"],
            letter_freq["S"],
            letter_freq["H"],
            letter_freq["R"],
            letter_freq["D"],
            letter_freq["L"],
            letter_freq["C"],
            letter_freq["U"],
            letter_freq["M"],
            letter_freq["W"],
            letter_freq["F"],
            letter_freq["G"],
            letter_freq["Y"],
            letter_freq[" "],
            # this is very stupid, i spent HOURS debugging but i didnt think of this.
            # space character is a very frequent character, i just follow wikipedia blindly
            # this is SO STUPID, lesson learned.
        ]
        score = sum(freq_letter_in_english)
        if score >= best_score:
            best_score = score
            final_string = string_

    return final_string


temp_list = []
for key_index in range(KEY_LENGTH):
    if len(possible_value_dict[key_index]) < 2:
        temp_list.append(possible_value_dict[key_index][0])
    else:
        temp_list.append(choose_based_on_freq_alphabet(possible_value_dict[key_index]))


def merge(value_list):
    # value_list = ['abcdef','123456']
    # return value: 'a1b2c3d4...'
    max_len = len(value_list[0])
    ans = []
    for char_index in range(0, max_len):
        for key_index in range(0, KEY_LENGTH):
            ans.append(value_list[key_index][char_index : char_index + 1])
    final = "".join(ans)
    return final


plain_message = merge(temp_list)
print(plain_message)
# f = open("output.txt", "w")
# f.write(plain_message)
# f.close()
