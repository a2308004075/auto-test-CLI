from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.swap_common_station import SwapCommonStation


class NcsSwapCommonStation:
    """
    nacos操作swap-common-station
    """

    @staticmethod
    @KwDecorator("nacos获取swap-common-station")
    def swap_common_station_get():
        return SwapCommonStation.swap_common_station_get()

    @staticmethod
    @KwDecorator("nacos配置swap-common-station：换电云接模拟器")
    def swap_common_station_post_1():
        content = """caes:
  swap:
    station:
      id: 202311161632108290000
      mqtt:
        swapCloud:
          url: ssl://exchangemqtts-test.catles.com:8883
          username: 202303141816596736507
          password: DJ3966fRvPyNGF1SdN8qNq
        dataCloud:
          url: ssl://exchangemqtts-test.catles.com:8883
          username: simulate-collect
          password: gREvMvwYG9cUYUj6QnhS
    core:
      stationModuleType: 31
    cloud-login:
      url: https://station-ops-b-test.catles.com/caesAdmin/operation
      appId: Z8UZ90YLGNHN29B7TJGQNG7VQ3OT46YN
      privateKey: MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgpfs8/zRRZFK4XXkOkYxh/OLNaT0XO7fay+uhPLn05aVSpds+atEJp6lVEHjeXVefAA/nYMZbCMdcP2qzO5fvQVy+SoJVcE9gnGDQiDT61lHw/mwhsnJHq4K6adCRjt7kvycQPKbjzH+J7l2+KOcWhtSILq49qpkEDRwFLAOEYRm8QmghHCGRHLaoZpt2+wP/cJxScpyC7KRXJAFARpxrpNehZkVzZtNvLuC1zBKQQxpNCGKPhZtQ+ppbySb8gpwMpasga3uT+ZpzWgTGLFpksBLFc/t/b9Omrri+rJVYqWkKAaeuXWA0WIV++eL32oqiI+QIwZlRjFidk5mYpVjrAgMBAAECggEBAIvkHaRfI0LhFrtfAiSyj8lgOmvfAYiywwYvXu+X/uKH+2+95+4xe/hpXKYrYuVX6Q4XMsIsXm41dc0ZmCOdeE+q3kUCgv49f5HEevX8Ng5cBRzToHuzdZp9eqgzrqCiBeyxnCWiez2Q/VqyDEWkPp86J+ayp54haX/CnqzOR/3EXR37K8TgDcQV61NrDJCN/yyH6S10B91nx3pYWvyvL0VNtet02H2O1SJniTg9UyiDrgoWsYXajZM7nvvLzgi3vODH9+ErM4NE0ghMx5BHpdptvHl4QoT+4QD7o5ZBeZIBM2WetzyHKbBtn3i6yqLqZh5oJl2WR2//9V6IVnnHbdkCgYEA9Em6W3TiO+v5K32SFwVMMhn19mDz2VQTs/JKPIkpQ3I8urcAfImq3sBxBvN0Rrp6xrqrUgTggBxUSxMbnLepEiu1mmjrY9Rbms48NPymmZp6vK+NQGAIjGOlolT84J+cHDQHbOEpm/4u3nRAc6lgWEkbvIxRBk1gwl5rpCTtke8CgYEAqFmzhcH4ONsixAcbqYVeWI2esDySsiYB6/vdpIVCOuB4YKDDp6UAWP9W48kx3xtXDHEEbnVRsgcy25WWfQUhSUflf49sg4EVaw1pfyVPVvqBGOu30Yqid+3MR65Kt8xHc8TWM04BcHar66ey/dXKkGcCJhZzxcWXc2PNSGhItMUCgYAt89CCc7I642CztaNNgUmcAxYpioNUVmR+bQ1Z5dNFRK/3z4Tf6GWkET8xt4of4+REjci8XP5+GtYgaS/AgyvipyY6LZJZ7RBuRm086mnMayq7Y6qGeYoiHnyB1Mrc1ilfhMoAyToyhdX7MpMNLsdY1CfLh/mV3ehdp7VH40ptMQKBgAIh0LI6+KfPrqsI5ALLm5xHfuEAg2MaNCAG+pGg1mvkd+HRZ2jyIAUAhtsvqyAGOp3/uGyls7kreitpw5QlwnwpGvD4ogkwU1Mdwl5H3K9fUM89/P/8X35hVpr5zBxzy9vdfFD+Beqkthyv7QZl9MDLbS2KT0EL9ZUSiIEIQRN5AoGBAN2D+pQRnSZj2laMvrZ+5j9GxeBtzIfvCGkE4Ae0Qb7xv4C7FMqikRycG6JRxczh1/Bi7rVyPz0Din570DzNpC2yddh2tMFH/vjUaSQB/g5Cy6DPdFwl6Rl+jz0pnr2UWB8OiZPTGs8Zwxl7qDx7B68OX7QAeqztnS1TKd+PxVX4
        """
        return SwapCommonStation.swap_common_station_post(content)

    @staticmethod
    @KwDecorator("nacos配置swap-common-station：换电云接云平台测试环境")
    def swap_common_station_post_2():
        content = """caes:
      swap:
        station:
          id: 202206291701335851538
          mqtt:
            swapCloud:
              url: ssl://exchangemqtts-test.catles.com:8883
              username: 202206291701335851538
              password: sDTntsqpCEGFMcqNfUbZ
            dataCloud:
              url: ssl://exchangemqtts-test.catles.com:8883
              username: simulate-collect
              password: gREvMvwYG9cUYUj6QnhS
        core:
          stationModuleType: 31
        cloud-login:
          url: https://station-ops-b-test.catles.com/caesAdmin/operation
          appId: Z8UZ90YLGNHN29B7TJGQNG7VQ3OT46YN
          privateKey: MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgpfs8/zRRZFK4XXkOkYxh/OLNaT0XO7fay+uhPLn05aVSpds+atEJp6lVEHjeXVefAA/nYMZbCMdcP2qzO5fvQVy+SoJVcE9gnGDQiDT61lHw/mwhsnJHq4K6adCRjt7kvycQPKbjzH+J7l2+KOcWhtSILq49qpkEDRwFLAOEYRm8QmghHCGRHLaoZpt2+wP/cJxScpyC7KRXJAFARpxrpNehZkVzZtNvLuC1zBKQQxpNCGKPhZtQ+ppbySb8gpwMpasga3uT+ZpzWgTGLFpksBLFc/t/b9Omrri+rJVYqWkKAaeuXWA0WIV++eL32oqiI+QIwZlRjFidk5mYpVjrAgMBAAECggEBAIvkHaRfI0LhFrtfAiSyj8lgOmvfAYiywwYvXu+X/uKH+2+95+4xe/hpXKYrYuVX6Q4XMsIsXm41dc0ZmCOdeE+q3kUCgv49f5HEevX8Ng5cBRzToHuzdZp9eqgzrqCiBeyxnCWiez2Q/VqyDEWkPp86J+ayp54haX/CnqzOR/3EXR37K8TgDcQV61NrDJCN/yyH6S10B91nx3pYWvyvL0VNtet02H2O1SJniTg9UyiDrgoWsYXajZM7nvvLzgi3vODH9+ErM4NE0ghMx5BHpdptvHl4QoT+4QD7o5ZBeZIBM2WetzyHKbBtn3i6yqLqZh5oJl2WR2//9V6IVnnHbdkCgYEA9Em6W3TiO+v5K32SFwVMMhn19mDz2VQTs/JKPIkpQ3I8urcAfImq3sBxBvN0Rrp6xrqrUgTggBxUSxMbnLepEiu1mmjrY9Rbms48NPymmZp6vK+NQGAIjGOlolT84J+cHDQHbOEpm/4u3nRAc6lgWEkbvIxRBk1gwl5rpCTtke8CgYEAqFmzhcH4ONsixAcbqYVeWI2esDySsiYB6/vdpIVCOuB4YKDDp6UAWP9W48kx3xtXDHEEbnVRsgcy25WWfQUhSUflf49sg4EVaw1pfyVPVvqBGOu30Yqid+3MR65Kt8xHc8TWM04BcHar66ey/dXKkGcCJhZzxcWXc2PNSGhItMUCgYAt89CCc7I642CztaNNgUmcAxYpioNUVmR+bQ1Z5dNFRK/3z4Tf6GWkET8xt4of4+REjci8XP5+GtYgaS/AgyvipyY6LZJZ7RBuRm086mnMayq7Y6qGeYoiHnyB1Mrc1ilfhMoAyToyhdX7MpMNLsdY1CfLh/mV3ehdp7VH40ptMQKBgAIh0LI6+KfPrqsI5ALLm5xHfuEAg2MaNCAG+pGg1mvkd+HRZ2jyIAUAhtsvqyAGOp3/uGyls7kreitpw5QlwnwpGvD4ogkwU1Mdwl5H3K9fUM89/P/8X35hVpr5zBxzy9vdfFD+Beqkthyv7QZl9MDLbS2KT0EL9ZUSiIEIQRN5AoGBAN2D+pQRnSZj2laMvrZ+5j9GxeBtzIfvCGkE4Ae0Qb7xv4C7FMqikRycG6JRxczh1/Bi7rVyPz0Din570DzNpC2yddh2tMFH/vjUaSQB/g5Cy6DPdFwl6Rl+jz0pnr2UWB8OiZPTGs8Zwxl7qDx7B68OX7QAeqztnS1TKd+PxVX4
            """
        return SwapCommonStation.swap_common_station_post(content)
