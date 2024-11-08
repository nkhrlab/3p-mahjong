#計算
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.hand_calculating.scores import ScoresCalculator
#麻雀牌
from mahjong.tile import TilesConverter
#役, オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
#鳴き
from mahjong.meld import Meld
#風(場&自)
from mahjong.constants import EAST, SOUTH, WEST, NORTH

#HandCalculator(計算用クラス)のインスタンスを生成
calculator = HandCalculator()

scores = ScoresCalculator()

#結果出力用
def print_hand_result(hand_result):
     #翻数, 符数
     print(hand_result.han, hand_result.fu)
     #点数(ツモアガリの場合[左：親失点, 右:子失点], ロンアガリの場合[左:放銃者失点, 右:0])
     # print(hand_result.cost['main'], result.cost['additional'])
     #役
     print(hand_result.yaku)
     #符数の詳細
     for fu_item in hand_result.fu_details:
          print(fu_item)
     print('')

rule_dict = {
    'has_open_tanyao': True,
    'has_aka_dora': False,
    'has_double_yakuman': True,
    'kiriage': True,
    'fu_for_open_pinfu': True,
    'fu_for_pinfu_tsumo': False,
    'renhou_as_yakuman': True,
    'has_daisharin': False,
    'has_daisharin_other_suits': False,
    'has_daichisei': False,
    'has_sashikomi_yakuman': False,
    'limit_to_sextuple_yakuman': True,
    'paarenchan_needs_yaku': True,
}
rule = OptionalRules(**rule_dict)

config_dict = {
     'is_tsumo': False,
     'is_riichi': False,
     'is_ippatsu': False,
     'is_rinshan': False,
     'is_chankan': False,
     'is_haitei': False,
     'is_houtei': False,
     'is_daburu_riichi': False,
     'is_nagashi_mangan': False,
     'is_tenhou': False,
     'is_renhou': False,
     'is_chiihou': False,
     'is_open_riichi': False,
     'player_wind': None,
     'round_wind': None,
     'kyoutaku_number': 0,
     'tsumi_number': 0,
     'paarenchan': 0,
     'options': rule,
     'player_wind': None,
     'round_wind': None,
}

#オプション(ツモを追加,Falseだとロン)
config = HandConfig(**config_dict)


#アガリ形(man=マンズ, pin=ピンズ, sou=ソーズ, honors=字牌)
tiles = TilesConverter.string_to_136_array(man='555', pin='555', sou='22555', honors='111')
#アガリ牌(上と同じ)
win_tile = TilesConverter.string_to_136_array(sou='5')[0]
#鳴き(なし)
melds = [
     Meld(Meld.PON, TilesConverter.string_to_136_array(man='555')),
]
#ドラ(なし)
dora_indicators = None

#計算
hand_result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
print(hand_result.han, hand_result.fu)
print(scores.calculate_scores(hand_result.han + 2, hand_result.fu, config))
# print_hand_result(result)