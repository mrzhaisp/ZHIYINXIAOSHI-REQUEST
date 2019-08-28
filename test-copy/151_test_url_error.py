#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.commonlib import Commonlib
c = Commonlib()
import requests
import time

video_id_list = [
4862,
4863,
4864,
4865,
4866,
4867,
5795,
5796,
5797,
5798,
5799,
5800,
5801,
5802,
5803,
5804,
5805,
5806,
5807,
5808,
5809,
5810,
5811,
5812,
5813,
5814,
5815,
5816,
5817,
5818,
5819,
5820,
5821,
5822,
5823,
5824,
5825,
5826,
5827,
5828,
5829,
5830,
5831,
5832,
5833,
5834,
5835,
5836,
5837,
5838,
5839,
5840,
5841,
5842,
5843,
5844,
5845,
5846,
5847,
5848,
5849,
5850,
5851,
5852,
5853,
5854,
5855,
5856,
5857,
5858,
5859,
5860,
6071,
6072,
6073,
6074,
6075,
6076,
6077,
6078,
6079,
6080,
6081,
6082,
6083,
6084,
6085,
6086,
6087,
6088,
6089,
6090,
6091,
6092,
6093,
6094,
6095,
6096,
6097,
6098,
6099,
6100,
6101,
6102,
6103,
6104,
6105,
6106,
6107,
6108,
6109,
6110,
6111,
6112,
6113,
6114,
6115,
6116,
6117,
6118,
6119,
6120,
6121,
6122,
6123,
6124,
6125,
6126,
6127,
6128,
6129,
6130,
6131,
6430,
6492,
6493,
6494,
6495,
6496,
6497,
6498,
6499,
6500,
6501,
6502,
6503,
6504,
6505,
6506,
6507,
6508,
6509,
6510,
6511,
6512,
6513,
6514,
6515,
6516,
6517,
6518,
6519,
6520,
6521,
6522,
6523,
6524,
6525,
6526,
6527,
6528,
6529,
6530,
6531,
6532,
6533,
6534,
6535,
6536,
6537,
6538,
6539,
6540,
6541,
6542,
6543,
6544,
6545,
6546,
6547,
6548,
6549,
6550,
6551,
6552,
6553,
6554,
6555,
6556,
6557,
6558,
6559,
6560,
6561,
6562,
6563,
6564,
6565,
6566,
6567,
6568,
6569,
6570,
6571,
6572,
6573,
6574,
6575,
6576,
6577,
6578,
6579,
6580,
6581,
6582,
6583,
6584,
6585,
6586,
6587,
6588,
6589,
6590,
6591,
6592,
6593,
6594,
6595,
6596,
6597,
6598,
6599,
6600,
6601,
6602,
6603,
6605,
6606,
6607,
6608,
6609,
6610,
6611,
6612,
6613,
6614,
6615,
6616,
6617,
6618,
6619,
6620,
6621,
6622,
6623,
6624,
6625,
6626,
6627,
6628,
6629,
6630,
6631,
6632,
6633,
6635,
6636,
6637,
6638,
6639,
6640,
6641,
6642,
6643,
6644,
6645,
6646,
6647,
6648,
6649,
6650,
6651,
6652,
6653,
6654,
6706,
6707,
6708,
6709,
6710,
6711,
6712,
6713,
6714,
6715,
6716,
6717,
6718,
6719,
6720,
6721,
6722,
6723,
6724,
6725,
6726,
6727,
6728,
6729,
6730,
6731,
6732,
6740,
6741,
6742,
6743,
6744,
6746,
6748,
6749,
6751,
6752,
6753,
6754,
6755,
6756,
6757,
6758,
6759,
6760,
6761,
6762,
6763,
6764,
6765,
6766,
6767,
6768,
6816,
6817,
6832,
6899,
6900,
7105,
7325,
7326,
7327,
7328,
7329,
7330,
7331,
7332,
7333,
7334,
7335,
7336,
7337,
7338,
7339,
7340,
7341,
7342,
7343,
7344,
7345,
7346,
7347,
7348,
7349,
7350,
7351,
7352,
7353,
7354,
7355,
7356,
7357,
7358,
7359,
7404,
7405,
7406,
7408,
7409,
7410,
7411,
7412,
7413,
7414,
7415,
7416,
7417,
7418,
7419,
7420,
7421,
7422,
7423,
7424,
7425,
7426,
7427,
7428,
7429,
7430,
7431,
7432,
7433,
7434,
7435,
7436,
7437,
7438,
7439,
7440,
7441,
7442,
7443,
7444,
7445,
7446,
7447,
7448,
7449,
7450,
7451,
7452,
7453,
7454,
7455,
7456,
7457,
7458,
7459,
7460,
7461,
7462,
7463,
7464,
7465,
7466,
7467,
7468,
7469,
7470,
7471,
7472,
7473,
7474,
7475,
7476,
7477,
7478,
7479,
7480,
7481,
7482,
7483,
7484,
7485,
7486,
7488,
7489,
7490,
7491,
7492,
7493,
7494,
7495,
7496,
7497,
7498,
7499,
7500,
7501,
7502,
7503,
7504,
7505,
7506,
7507,
7508,
7509,
7510,
7511,
7512,
7513,
7514,
7515,
7516,
7517,
7518,
7519,
7520,
7521,
7522,
7523,
7524,
7525,
7526,
7527,
7528,
7529,
7530,
7531,
7532,
7533,
7534,
7535,
7536,
7537,
7539,
7540,
7541,
7542,
7543,
7544,
7545,
7546,
7547,
7548,
7549,
7550,
7551,
7552,
7553,
7554,
7555,
7556,
7557,
7558,
7559,
7560,
7561,
7562,
7563,
7564,
7565,
7566,
7567,
7568,
7569,
7570,
7571,
7572,
7573,
7574,
7575,
7576,
7577,
7578,
7579,
7580,
7581,
7582,
7583,
7584,
7585,
7586,
7587,
7588,
7589,
7590,
7591,
7592,
7593,
7594,
7595,
7596,
7597,
7598,
7599,
7600,
7601,
7602,
7603,
7604,
7605,
7606,
7607,
7608,
7609,
7610,
7611,
7612,
7613,
7614,
7615,
7616,
7617,
7618,
7619,
7620,
7621,
7622,
7623,
7624,
7625,
7626,
7627,
7628,
7629,
7630,
7631,
7632,
7633,
7634,
7635,
7636,
7637,
7638,
7639,
7640,
7641,
7642,
7643,
7644,
7645,
7646,
7647,
7648,
7649,
7650,
7651,
7652,
7653,
7654,
7655,
7656,
7657,
7658,
7659,
7660,
7661,
7662,
7663,
7665,
7666,
7671,
7672,
7673,
7674,
7675,
7677,
7680,
7682,
7683,
7685,
7688,
7690,
7692,
7693,
7694,
7696,
7697,
7698,
7699,
7701,
7702,
7703,
7704,
7705,
7707,
7708,
7711,
7712,
7713,
7718,
7719,
7720,
7721,
7722,
7723,
7724,
7725,
7726,
7727,
7728,
7729,
7730,
7731,
7732,
7734,
7735,
7737,
7738,
7739,
7741,
7742,
7750,
7753,
7756,
7757,
7758,
7759,
7760,
7761,
7762,
7764,
7766,
7767,
7768,
7770,
7771,
7773,
7774,
7776,
7778,
7779,
7780,
7782,
7783,
7784,
7785,
7786,
7789,
7793,
7794,
7795,
7796,
7798,
7800,
7802,
7804,
7808,
7809,
7813,
7814,
7818,
7820,
7823,
7824,
7825,
7827,
7828,
7829,
7830,
7832,
7834,
7835,
7836,
7839,
7840,
7843,
7844,
7845,
7846,
7847,
7848,
7849,
7851,
7852,
7853,
7854,
7855,
7858,
7859,
7860,
7862,
7863,
7864,
7865,
7867,
7869,
7870,
7871,
7872,
7874,
7877,
7879,
7885,
7891,
7892,
7893,
7894,
7895,
7897,
7898,
7899,
7902,
7904,
7910,
7913,
7914,
7916,
7919,
7920,
7921,
7926,
7927,
7929,
7931,
7932,
7934,
7936,
7937,
7938,
7941,
7942,
7943,
7944,
7945,
7946,
7947,
7952,
7954,
7956,
7957,
7959,
7960,
7962,
7963,
7967,
7969,
7970,
7973,
7977,
7983,
7989,
7990,
7991,
7992,
7998,
7999,
8001,
8005,
8008,
8014,
8015,
8019,
8021,
8022,
8024,
8026,
8028,
8031,
8032,
8033,
8035,
8036,
8039,
8042,
8044,
8045,
8049,
8050,
8051,
8052,
8055,
8056,
8057,
8058,
8059,
8060,
8061,
8062,
8063,
8065,
8066,
8068,
8069,
8072,
8073,
8075,
8077,
8079,
8080,
8081,
8084,
8085,
8087,
8088,
8090,
8092,
8093,
8095,
8096,
8098,
8099,
8100,
8102,
8103,
8105,
8106,
8107,
8109,
8110,
8111,
8112,
8113,
8114,
8115,
8116,
8117,
8119,
8120,
8122,
8123,
8124,
8125,
8127,
8130,
8131,
8132,
8133,
8134,
8138,
8139,
8140,
8141,
8142,
8145,
8148,
8151,
8152,
8154,
8156,
8159,
8160,
8161,
8162,
8164,
8169,
8171,
8174,
8175,
8177,
8178,
8179,
8180,
8181,
8182,
8183,
8184,
8186,
8187,
8188,
8189,
8190,
8192,
8194,
8196,
8198,
8199,
8200,
8202,
8203,
8204,
8205,
8208,
8209,
8210,
8211,
8213,
8214,
8215,
8216,
8218,
8220,
8222,
8224,
8227,
8228,
8231,
8233,
8237,
8238,
8240,
8241,
8242,
8245,
8247,
8248,
8249,
8250,
8253,
8254,
8256,
8257,
8259,
8260,
8262,
8263,
8264,
8265,
8268,
8269,
8271,
8272,
8273,
8274,
8275,
8276,
8278,
8279,
8280,
8283,
8287,
8289,
8290,
8291,
8294,
8295,
8296,
8299,
8300,
8301,
8302,
8304,
8305,
8308,
8309,
8313,
8314,
8316,
8317,
8320,
8322,
8323,
8324,
8325,
8327,
8328,
8329,
8330,
8331,
8332,
8333,
8334,
8335,
8336,
8337,
8338,
8339,
8340,
8341,
8342,
8343,
8344,
8345,
8346,
8347,
8348,
8350,
8351,
8353,
8354,
8355,
8356,
8357,
8358,
8359,
8360,
8361,
8362,
8363,
8365,
8366,
8367,
8368,
8369,
8370,
8371,
8372,
8373,
8374,
8375,
8376,
8377,
8378,
8379,
8380,
8381,
8382,
8383,
8385,
8386,
8387,
8388,
8389,
8390,
8391,
8392,
8393,
8394,
8395,
8396,
8397,
8398,
8399,
8400,
8401,
8402,
8403,
8404,
8405,
8406,
8408,
8409,
8410,
8411,
8412,
8413,
8414,
8415,
8417,
8418,
8421,
8422,
8424,
8425,
8426,
8427,
8428,
8430,
8431,
8432,
8433,
8434,
8436,
8439,
8440,
8442,
8444,
8445,
8447,
8448,
8449,
8451,
8453,
8454,
8455,
8456,
8457,
8458,
8461,
8463,
8465,
8466,
8467,
8469,
8470,
8471,
8472,
8473,
8475,
8478,
8481,
8482,
8483,
8485,
8486,
8487,
8488,
8491,
8492,
8493,
8497,
8498,
8499,
8502,
8504,
8505,
8506,
8507,
8508,
8510,
8516,
8518,
8519,
8522,
8525,
8528,
8531,
8533,
8534,
8535,
8539,
8540,
8542,
8544,
8545,
8546,
8549,
8550,
8553,
8554,
8556,
8557,
8559,
8560,
8564,
8565,
8566,
8568,
8572,
8573,
8574,
8576,
8578,
8580,
8586,
8587,
8591,
8592,
8593,
8594,
8595,
8597,
8598,
8599,
8600,
8601,
8605,
8606,
8607,
8610,
8611,
8613,
8619,
8620,
8621,
8622,
8627,
8629,
8630,
8633,
8634,
8638,
8640,
8641,
8642,
8645,
8648,
8653,
8655,
8658,
8662,
8665,
8667,
8668,
8672,
8674,
8676,
8677,
8679,
8682,
8683,
8685,
8688,
8690,
8691,
8693,
8694,
8695,
8696,
8697,
8699,
8700,
8701,
8702,
8703,
8704,
8706,
8709,
8715,
8718,
8720,
8724,
8725,
8727,
8728,
8730,
8734,
8735,
8736,
8737,
8739,
8741,
8745,
8746,
8748,
8751,
8752,
8753,
8756,
8760,
8761,
8762,
8768,
8770,
8771,
8776,
8778,
8780,
8781,
8782,
8783,
8785,
8789,
8790,
8792,
8794,
8795,
8802,
8803,
8805,
8807,
8808,
8809,
8810,
8811,
8812,
8814,
8816,
8819,
8820,
8822,
8823,
8825,
8828,
8830,
8831,
8832,
8833,
8835,
8836,
8837,
8838,
8839,
8840,
8841,
8843,
8844,
8847,
8852,
8854,
8855,
8860,
8861,
8867,
8869,
8870,
8871,
8872,
8873,
8874,
8877,
8879,
8880,
8883,
8887,
8888,
8889,
8893,
8894,
8898,
8901,
8903,
8904,
8906,
8907,
8908,
8910,
8915,
8917,
8918,
8921,
8922,
8923,
8924,
8925,
8926,
8927,
8928,
8929,
8930,
8932,
8933,
8934,
8935,
8937,
8938,
8939,
8940,
8942,
8943,
8945,
8946,
8947,
8948,
8949,
8950,
8951,
8952,
8954,
8955,
8957,
8958,
8959,
8960,
8962,
8963,
8964,
8966,
8967,
8968,
8969,
8970,
8972,
8973,
8974,
8978,
8979,
8980,
8981,
8982,
8983,
8984,
8985,
8987,
8988,
8989,
8990,
8992,
8993,
8996,
8997,
8998,
8999,
9000,
9002,
9003,
9004,
9005,
9006,
9007,
9010,
9012,
9013,
9014,
9016,
9017,
9018,
9019,
9021,
9022,
9023,
9024,
9026,
9030,
9032,
9034,
9035,
9036,
9037,
9038,
9040,
9041,
9042,
9043,
9044,
9045,
9046,
9049,
9051,
9053,
9054,
9055,
9056,
9057,
9058,
9059,
9060,
9061,
9064,
9065,
9066,
9067,
9068,
9069,
9070,
9071,
9072,
9073,
9074,
9075,
9076,
9077,
9078,
9079,
9080,
9081,
9083,
9084,
9085,
9088,
9089,
9091,
9092,
9093,
9094,
9096,
9097,
9098,
9099,
9100,
9101,
9103,
9104,
9107,
9108,
9109,
9110,
9112,
9114,
9115,
9116,
9117,
9118,
9121,
9122,
9123,
9124,
9125,
9126,
9127,
9128,
9129,
9130,
9131,
9132,
9133,
9135,
9136,
9995,
9996,
9998,
10000,
10001,
10006,
10007,
10010,
10011,
10012,
10016,
10017,
10018,
10019,
10020,
10022,
10023,
10024,
10025,
10027,
10028,
10029,
10031,
10032,
10033,
10035,
10036,
10038,
10039,
10040,
10042,
10045,
10046,
10048,
10049,
10050,
10053,
10054,
10056,
10057,
10058,
10060,
10061,
10062,
10063,
10064,
10065,
10066,
10068,
10069,
10070,
10071,
10072,
10073,
10075,
10077,
10080,
10082,
10083,
10084,
10086,
10087,
10088,
10089,
10090,
10091,
10093,
10097,
10098,
10099,
10100,
10101,
10102,
10105,
10106,
10112,
10113,
10115,
10116,
10117,
10118,
10119,
10120,
10121,
10122,
10123,
10124,
10125,
10126,
10127,
10128,
10129,
10130,
10131,
10132,
10133,
10134,
10135,
10136,
10137,
10138,
10139,
10140,
10141,
10142,
10143,
10144,
10145,
10146,
10147,
10148,
10149,
10150,
10151,
10152,
10153,
10154,
10155,
10156,
10157,
10158,
10159,
10160,
10161,
10162,
10163,
10164,
10484,
10485,
10486,
10487,
10488,
10489,
10580,
10581,
10582,
10583,
10584,
10585,
10586,
10587,
10588,
10589,
10590,
10591,
10592,
10593,
10594,
10595,
10596,
10597,
10598,
10599,
10600,
10601,
10602,
10603,
10604,
10606,
10607,
10608,
10609,
10610,
10612,
10613,
10614,
10615,
10617,
10618,
10619,
10621,
10622,
10623,
10624,
10625,
10626,
10627,
10628,
10629,
10630,
10631,
10632,
10633,
10634,
10635,
10636,
10637,
10638,
10639,
10640,
10641,
10642,
10643,
10644,
10645,
10646,
10647,
10648,
10649,
10650,
10651,
10652,
10655,
10656,
10657,
10658,
10659,
10660,
10661,
10662,
10664,
10665,
10666,
10667,
10669,
10670,
10671,
10672,
10673,
10677,
10678,
10679,
10680,
10681,
10682,
10684,
10685,
10686,
10687,
10688,
10689,
10690,
10691,
10692,
10693,
10694,
10695,
10696,
10697,
10698,
10699,
10700,
10702,
10703,
10704,
10706,
10707,
10708,
10709,
10710,
10711,
10712,
10713,
10714,
10715,
10716,
10717,
10718,
10719,
10720,
10721,
10722,
10723,
10724,
10725,
10726,
10727,
10728,
10729,
10730,
10731,
10732,
10733,
10734,
10735,
10736,
10737,
10738,
10739,
10740,
10741,
10742,
10743,
10744,
10745,
10746,
10747,
10748,
10749,
10750,
10751,
10752,
10753,
10754,
10755,
10756,
10758,
10759,
10760,
10761,
10762,
10763,
10764,
10765,
10766,
10767,
10768,
10769,
10770,
10771,
10772,
10773,
10774,
10775,
10776,
10777,
10778,
10779,
10780,
10781,
10782,
10783,
10784,
10785,
10786,
10787,
10788,
10789,
10790,
10791,
10792,
10793,
10794,
10795,
10796,
10797,
10798,
10799,
10800,
10801,
10803,
10804,
10805,
10807,
10808,
10809,
10810,
10811,
10812,
10813,
10814,
10815,
10816,
10817,
10818,
10819,
10820,
10821,
10822,
10823,
10824,
10825,
10826,
10827,
10828,
10829,
10830,
10831,
10832,
10833,
10834,
10835,
10836,
10837,
10838,
10839,
10840,
10841,
10842,
10843,
10844,
10845,
10846,
10847,
10849,
10850,
10851,
10852,
10853,
10854,
10855,
10856,
10857,
10858,
10859,
10860,
10861,
10862,
10863,
10864,
10865,
10866,
10867,
10868,
10869,
10870,
10871,
10872,
10873,
10874,
10875,
10876,
10877,
10878,
10879,
10880,
10881,
10882,
10883,
10884,
10885,
10886,
10887,
10888,
10889,
10890,
10891,
10892,
10893,
10894,
10895,
10896,
10897,
10898,
10899,
10900,
10901,
10902,
10903,
10904,
10905,
10906,
10907,
10908,
10909,
10910,
10911,
10912,
10913,
10914,
10916,
10917,
10918,
10919,
10920,
10921,
10922,
10923,
10924,
10925,
10926,
10927,
10928,
10929,
10930,
10931,
10932,
10933,
10935,
10936,
10937,
10938,
10939,
10940,
10941,
10942,
10943,
10944,
10945,
10946,
10947,
10948,
10949,
10950,
10951,
10952,
10953,
10954,
10956,
10957,
10959,
10961,
10962,
10963,
10965,
10967,
10968,
10969,
10972,
10974,
10976,
10977,
10978,
10979,
10981,
10982,
10983,
10984,
10985,
10986,
10988,
10989,
10990,
10991,
10993,
10994,
10996,
10997,
10999,
11000,
11001,
11002,
11003,
11004,
11005,
11006,
11007,
11008,
11009,
11010,
11011,
11012,
11013,
11014,
11015,
11016,
11017,
11018,
11019,
11020,
11021,
11022,
11023,
11025,
11026,
11027,
11028,
11029,
11030,
11031,
11032,
11033,
11034,
11035,
11037,
11038,
11039,
11040,
11041,
11042,
11043,
11045,
11046,
11047,
11048,
11049,
11050,
11051,
11052,
11053,
11054,
11055,
11056,
11057,
11058,
11059,
11060,
11061,
11062,
11063,
11064,
11065,
11066,
11067,
11068,
11069,
11070,
11071,
11072,
11073,
11074,
11075,
11076,
11077,
11078,
11079,
11080,
11082,
11083,
11085,
11086,
11087,
11088,
11089,
11090,
11091,
11092,
11093,
11094,
11095,
11096,
11097,
11098,
11099,
11100,
11101,
11102,
11103,
11104,
11105,
11106,
11107,
11108,
11109,
11110,
11111,
11112,
11113,
11114,
11115,
11116,
11117,
11118,
11119,
11120,
11121,
11122,
11125,
11126,
11128,
11129,
11130,
11131,
11132,
11133,
11134,
11135,
11136,
11137,
11138,
11139,
11140,
11141,
11142,
11143,
11144,
11145,
11146,
11147,
11148,
11149,
11150,
11151,
11152,
11153,
11154,
11155,
11156,
11158,
11159,
11160,
11161,
11162,
11163,
11164,
11165,
11166,
11167,
11168,
11169,
11170,
11171,
11172,
11173,
11174,
11175,
11176,
11177,
11178,
11179,
11180,
11181,
11182,
11183,
11184,
11185,
11186,
11187,
11188,
11189,
11190,
11235,
11236,
11237,
11238,
11239,
11240,
11241,
11242,
11243,
11244,
11245,
11246,
11247,
11248,
11249,
11250,
11251,
11252,
11254,
11256,
11257,
11258,
11260,
11261,
11262,
11263,
11264,
11265,
11266,
11267,
11268,
11269,
11270,
11271,
11272,
11275,
11276,
11277,
11279,
11281,
11282,
11283,
11284,
11285,
11287,
11289,
11290,
11291,
11292,
11293,
11294,
11295,
11296,
11297,
11298,
11299,
11300,
11301,
11302,
11303,
11304,
11305,
11306,
11307,
11308,
11309,
11310,
11311,
11312,
11313,
11314,
11315,
11316,
11317,
11318,
11319,
11320,
11321,
11323,
11324,
11325,
11326,
11327,
11328,
11329,
11330,
11331,
11332,
11333,
11334,
11335,
11336,
11337,
11338,
11339,
11340,
11341,
11342,
11343,
11344,
11345,
11346,
11347,
11348,
11349,
11350,
11351,
11353,
11354,
11355,
11356,
11357,
11358,
11359,
11360,
11361,
11362,
11363,
11364,
11365,
11366,
11367,
11368,
11369,
11370,
11371,
11372,
11373,
11374,
11375,
11376,
11377,
11378,
11379,
11380,
11381,
11382,
11383,
11384,
11385,
11386,
11387,
11388,
11389,
11390,
11391,
11392,
11393,
11394,
11395,
11396,
11397,
11398,
11399,
11400,
11401,
11402,
11403,
11404,
11405,
11406,
11407,
11408,
11409,
11410,
11411,
11412,
11413,
11414,
11415,
11416,
11417,
11418,
11419,
11420,
11421,
11422,
11423,
11424,
11425,
11426,
11427,
11429,
11430,
11431,
11432,
11433,
11434,
11435,
11436,
11437,
11438,
11439,
11440,
11441,
11442,
11443,
11444,
11445,
11446,
11447,
11448,
11449,
11450,
11451,
11452,
11453,
11454,
11455,
11456,
11457,
11458,
11459,
11460,
11461,
11462,
11463,
11464,
11465,
11466,
11467,
11468,
11469,
11470,
11471,
11472,
11473,
11474,
11475,
11476,
11477,
11478,
11479,
11480,
11481,
11482,
11483,
11484,
11485,
11486,
11487,
11488,
11489,
11490,
11491,
11492,
11493,
11494,
11495,
11497,
11498,
11499,
11500,
11501,
11502,
11503,
11504,
11505,
11506,
11507,
11508,
11509,
11510,
11511,
11512,
11513,
11514,
11515,
11516,
11517,
11518,
11519,
11520,
11521,
11522,
11523,
11524,
11525,
11526,
11527,
11528,
11529,
11530,
11531,
11532,
11533,
11534,
11535,
11536,
11537,
11538,
11539,
11540,
11541,
11542,
11543,
11544,
11545,
11546,
11547,
11548,
11549,
11550,
11551,
11552,
11553,
11554,
11555,
11556,
11557,
11558,
11559,
11560,
11561,
11562,
11563,
11564,
11565,
11566,
11567,
11568,
11570,
11571,
11572,
11573,
11574,
11575,
11577,
11578,
11579,
11580,
11581,
11582,
11583,
11584,
11585,
11586,
11587,
11588,
11589,
11590,
11591,
11592,
11593,
11594,
11595,
11596,
11597,
11598,
11599,
11600,
11601,
11602,
11603,
11604,
11605,
11606,
11607,
11608,
11609,
11610,
11611,
11613,
11614,
11615,
11617,
11618,
11619,
11620,
11621,
11622,
11623,
11624,
11625,
11626,
11627,
11628,
11629,
11630,
11631,
11632,
11633,
11634,
11635,
11636,
11637,
11638,
11639,
11640,
11641,
11642,
11643,
11644,
11645,
11646,
11647,
11648,
11649,
11651,
11652,
11653,
11654,
11655,
11656,
11657,
11658,
11659,
11661,
11662,
11663,
11664,
11665,
11666,
11667,
11668,
11669,
11670,
11671,
11672,
11673,
11674,
11675,
11676,
11677,
11678,
11679,
11680,
11681,
11682,
11683,
11684,
11685,
11686,
11687,
11688,
11689,
11690,
11691,
11692,
11693,
11694,
11695,
11696,
11697,
11698,
11699,
11702,
11703,
11704,
11705,
11706,
11707,
11708,
11709,
11710,
11711,
11712,
11713,
11714,
11715,
11716,
11717,
11718,
11720,
11721,
11722,
11724,
11725,
11726,
11727,
11728,
11729,
11730,
11731,
11732,
11733,
11734,
11735,
11736,
11737,
11738,
11740,
11741,
11742,
11743,
11744,
11745,
11746,
11747,
11748,
11749,
11750,
11751,
11752,
11753,
11754,
11755,
11756,
11757,
11758,
11759,
11760,
11761,
11762,
11763,
11764,
11765,
11766,
11767,
11768,
11769,
11770,
11771,
11772,
11773,
11774,
11776,
11777,
11778,
11779,
11780,
11781,
11782,
11783,
11784,
11785,
11786,
11787,
11788,
11789,
11790,
11791,
11792,
11793,
11794,
11795,
11796,
11797,
11798,
11799,
11800,
11801,
11802,
11804,
11805,
11806,
11807,
11808,
11809,
11810,
11811,
11812,
11814,
11815,
11817,
11818,
11819,
11820,
11821,
11822,
11823,
11824,
11825,
11826,
11827,
11828,
11829,
11830,
11831,
11832,
11833,
11834,
11835,
11836,
11837,
11838,
11839,
11840,
11841,
11842,
11843,
11844,
11845,
11846,
11847,
11848,
11849,
11850,
11851,
11852,
11854,
11855,
11856,
11857,
11858,
11859,
11861,
11862,
11863,
11864,
11865,
11866,
11867,
11868,
11869,
11870,
11871,
11872,
11873,
11874,
11875,
11876,
11877,
11878,
11879,
11880,
11881,
11882,
11883,
11884,
11885,
11886,
11887,
11888,
11889,
11890,
11891,
11892,
11893,
11894,
11896,
11897,
11898,
11899,
11900,
11901,
11902,
11903,
11904,
11905,
11906,
11907,
11908,
11909,
11910,
11911,
11912,
11913,
11914,
11915,
11916,
11917,
11918,
11919,
11920,
11921,
11922,
11923,
11924,
11925,
11926,
11927,
11928,
11929,
11930,
11931,
11932,
11933,
11934,
11935,
11936,
11937,
11938,
11939,
11940,
11941,
11942,
11943,
11944,
11945,
11946,
11947,
11949,
11950,
11951,
11952,
11953,
11954,
11955,
11956,
11958,
11959,
11960,
11961,
11962,
11963,
11964,
11965,
11966,
11967,
11968,
11969,
11970,
11971,
11972,
11973,
11974,
11975,
11976,
11977,
11978,
11979,
11980,
11981,
11982,
11983,
11984,
11985,
11986,
11987,
11988,
11989,
11990,
11991,
11992,
11993,
11994,
11995,
11996,
11997,
11998,
11999,
12000,
12001,
12002,
12003,
12004,
12005,
12006,
12007,
12009,
12010,
12012,
12013,
12014,
12015,
12016,
12017,
12018,
12019,
12020,
12022,
12023,
12026,
12027,
12028,
12029,
12030,
12031,
12032,
12033,
12034,
12035,
12036,
12037,
12038,
12039,
12040,
12041,
12042,
12043,
12044,
12045,
12046,
12047,
12048,
12050,
12051,
12052,
12053,
12055,
12056,
12057,
12058,
12059,
12060,
12061,
12062,
12063,
12064,
12065,
12066,
12069,
12070,
12071,
12072,
12075,
12076,
12077,
12078,
12079,
12080,
12081,
12082,
12083,
12084,
12085,
12088,
12089,
12090,
12091,
12092,
12094,
12095,
12096,
12097,
12098,
12099,
12100,
12101,
12102,
12103,
12104,
12105,
12106,
12107,
12108,
12109,
12110,
12111,
12112,
12113,
12114,
12115,
12116,
12117,
12118,
12119,
12121,
12122,
12123,
12124,
12127,
12128,
12129,
12130,
12131,
12133,
12134,
12135,
12136,
12137,
12138,
12139,
12140,
12141,
12142,
12143,
12144,
12145,
12146,
12147,
12148,
12149,
12150,
12151,
12152,
12153,
12154,
12155,
12156,
12157,
12158,
12159,
12160,
12161,
12162,
12163,
12165,
12167,
12168,
12169,
12170,
12171,
12172,
12173,
12174,
12175,
12176,
12177,
12178,
12179,
12180,
12181,
12183,
12185,
12186,
12187,
12188,
12189,
12190,
12191,
12192,
12193,
12194,
12195,
12196,
12197,
12198,
12199,
12200,
12201,
12202,
12203,
12205,
12206,
12207,
12208,
12209,
12210,
12211,
12212,
12213,
12214,
12215,
12216,
12217,
12218,
12220,
12221,
12222,
12223,
12224,
12225,
12226,
12227,
12228,
12230,
12231,
12232,
12233,
12234,
12235,
12236,
12237,
12238,
12239,
12240,
12241,
12242,
12243,
12244,
12245,
12246,
12247,
12248,
12249,
12250,
12251,
12253,
12254,
12255,
12256,
12257,
12258,
12260,
12261,
12262,
12263,
12264,
12265,
12266,
12267,
12268,
12269,
12270,
12271,
12272,
12273,
12275,
12276,
12277,
12278,
12280,
12281,
12283,
12285,
12286,
12287,
12288,
12289,
12290,
12291,
12292,
12293,
12294,
12295,
12296,
12297,
12298,
12299,
12300,
12301,
12302,
12303,
12304,
12305,
12306,
12307,
12309,
12310,
12311,
12312,
12313,
12314,
12315,
12317,
12318,
12319,
12320,
12321,
12322,
12323,
12324,
12325,
12326,
12327,
12328,
12329,
12331,
12332,
12333,
12334,
12335,
12336,
12337,
12338,
12339,
12341,
12342,
12343,
12344,
12345,
12346,
12347,
12349,
12350,
12351,
12352,
12353,
12355,
12356,
12358,
12359,
12360,
12361,
12362,
12363,
12364,
12365,
12366,
12367,
12368,
12370,
12371,
12372,
12373,
12375,
12377,
12378,
12379,
12381,
12382,
12383,
12384,
12385,
12386,
12388,
12389,
12390,
12391,
12392,
12394,
12395,
12396,
12397,
12398,
12401,
12402,
12403,
12404,
12405,
12406,
12407,
12408,
12409,
12410,
12411,
12412,
12413,
12414,
12415,
12416,
12417,
12418,
12419,
12420,
12421,
12422,
12423,
12424,
12425,
12426,
12427,
12428,
12429,
12430,
12431,
12432,
12433,
12434,
12435,
12436,
12437,
12438,
12439,
12440,
12441,
12442,
12443,
12444,
12445,
12446,
12447,
12448,
12449,
12450,
12451,
12452,
12453,
12454,
12455,
12456,
12457,
12458,
12459,
12460,
12461,
12462,
12463,
12464,
12465,
12466,
12467,
12468,
12469,
12471,
12472,
12473,
12474,
12475,
12476,
12477,
12478,
12479,
12480,
12481,
12483,
12484,
12485,
12486,
12487,
12488,
12489,
12490,
12491,
12492,
12493,
12494,
12495,
12497,
12498,
12500,
12501,
12502,
12504,
12505,
12506,
12507,
12508,
12509,
12510,
12511,
12512,
12513,
12514,
12515,
12516,
12517,
12518,
12519,
12521,
12522,
12523,
12524,
12525,
12526,
12527,
12528,
12530,
12531,
12532,
12533,
12534,
12535,
12536,
12537,
12538,
12539,
12540,
12541,
12542,
12543,
12544,
12545,
12546,
12547,
12548,
12550,
12551,
12552,
12553,
12554,
12555,
12556,
12557,
12559,
12560,
12561,
12562,
12563,
12564,
12565,
12566,
12567,
12568,
12569,
12570,
12571,
12572,
12573,
12574,
12575,
12576,
12577,
12578,
12579,
12580,
12581,
12582,
12583,
12584,
12585,
12586,
12588,
12589,
12590,
12591,
12592,
12593,
12594,
12595,
12596,
12598,
12599,
12600,
12601,
12602,
12603,
12604,
12605,
12606,
12607,
12608,
12609,
12610,
12611,
12612,
12613,
12614,
12615,
12616,
12617,
12618,
12619,
12620,
12621,
12622,
12623,
12624,
12625,
12626,
12627,
12628,
12629,
12630,
12631,
12632,
12633,
12634,
12635,
12636,
12637,
12639,
12641,
12642,
12643,
12644,
12645,
12646,
12647,
12648,
12649,
12650,
12651,
12652,
12653,
12654,
12655,
12656,
12657,
12658,
12659,
12660,
12661,
12662,
12663,
12664,
12665,
12666,
12667,
12668,
12669,
12670,
12671,
12672,
12673,
12674,
12675,
12676,
12677,
12678,
12679,
12680,
12681,
12682,
12683,
12684,
12685,
12686,
12687,
12688,
12689,
12690,
12691,
12692,
12693,
12694,
12695,
12696,
12697,
12698,
12699,
12700,
12701,
12702,
12703,
12704,
12705,
12706,
12707,
12708,
12709,
12710,
12711,
12712,
12713,
12714,
12715,
12716,
12717,
12718,
12719,
12720,
12721,
12722,
12723,
12724,
12725,
12726,
12727,
12728,
12729,
12730,
12731,
12732,
12733,
12734,
12735,
12736,
12737,
12738,
12739,
12740,
12741,
12742,
12743,
12744,
12745,
12746,
12747,
12748,
12749,
12750,
12751,
12752,
12753,
12754,
12755,
12756,
12757,
12758,
12759,
12760,
12761,
12762,
12763,
12764,
12765,
12766,
12767,
12768,
12769,
12770,
12771,
12772,
12773,
12774,
12775,
12776,
12777,
12778,
12779,
12780,
12781,
12782,
12783,
12784,
12785,
12786,
12787,
12788,
12789,
12790,
12791,
12792,
12793,
12794,
12795,
12796,
12797,
12798,
12799,
12800,
12838,
12839,
12840,
12842,
12844,
12845,
12846,
12847,
12848,
12849,
12850,
12851,
12852,
12853,
12854,
12855,
12861,
12862,
12863,
12864,
12865,
12866,
12867,
12868,
12869,
12873,
12876,
12877,
12879,
12881,
12884,
12885,
12887,
12889,
12891,
12892,
12916,
12917,
12918,
12919,
12920,
12922,
12923,
12924,
12925,
12926,
12927,
12928,
12929,
12930,
12931,
12932,
12933,
12934,
12935,
12937,
12938,
12939,
12940,
12941,
13072,
13073,
13074,
13076,
13077,
13078,
13080,
13086,
13087,
13088,
13089,
13090,
13091,
13092,
13093,
13094,
13097,
13098,
13100,
13101,
13109,
13111,
13112,
13116,
13135,
13136,
13137,
13138,
13139,
13140,
13141,
13143,
13144,
13145,
13146,
13147,
13148,
13149,
13150,
13154,
13155,
13158,
13160,
13161,
13162,
13163,
13164,
13165,
13166,
13168,
13169,
13170,
13171,
13172,
13173,
13174,
13175,
13176,
13177,
13178,
13179,
13182,
13183,
13184,
13185,
13186,
13187,
13188,
13189,
13190,
13191,
13443,
13444,
13445,
13446,
13447,
13448,
13449,
13450,
13451,
13452,
13453,
13454,
13455,
13456,
13457,
13458,
13459,
13460,
13461,
13462,
13463,
13464,
13465,
13466,
13467,
13468,
13469,
13470,
13471,
13472,
13473,
14567,
14607,
14608]
base_host = "http://10.168.103.151/video_analysis/video_origin/getEntityById?id="

def get_all_url_list():
	"""组装所有的url列表"""
	video_url_list = []
	for id in video_id_list:
		req_url = base_host + str(id)
		video_url_list.append(req_url)
	# print(video_url_list)
	# print(len(video_url_list))
	return video_url_list

def get_error_id():
	"""拿到所有的url连接，分别去请求，如果没有请求到数据则切割url拿到id'加入到列表"""
	id_list = []
	for one_url in get_all_url_list():
		time.sleep(0.1)
		print(one_url)
		res = requests.get(one_url,cookies=c.get_cookie())
		content_uni = res.json()
		if  content_uni:
			#如果请求没返回正常内容 则加入  id 列表
			noaval_id = one_url.split('getEntityById?id=')[1]
			id_list.append(noaval_id)
			title = content_uni['title']
			print(id_list)
		else:
			pass

	time.sleep(0.1)
	print(id_list)

if __name__ == '__main__':
	get_error_id()

