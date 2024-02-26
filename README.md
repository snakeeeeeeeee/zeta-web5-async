# Zetachain XP Automation

## Описание
**Код может выполнить следующее:**

- **Enroll, Enroll verify** - полная регистрация с верификацей в кампании +2000 XP один раз. Встроенная реф ссылка.
- Выполнение квеста **Send & Receive ZETA in Zetachain** +3500 XP
- Выполнение квеста **Receive BNB in ZetaChain** +2500 XP
- Выполнение квеста **LP any core pool** +5000 XP
- Выполнение квеста **Receive BTC** +2500 XP
- Выполнение квеста **Receive ETH** +2500 XP
- Парсинг **XP, RANK, LEVEL** профиля
- **Клейм** всех доступных выполненных квестов
- Поддержка мультиаккаунтов


## Структура


- **config.py**: Файл-конфиг, где можно подстроить индивидуальные рабочие значения.

- **contracts_abi.py**: ABI контрактов.

- **functions.py**: Все функции, используемые в скрипте.

- **main.py**: Основной файл для запуска.

- **keys.txt**: Сюда нужно загрузить приватные ключи с нужным балансом ZETA в Zetachain и BNB в Binance Smart Chain.

- **fail_logs.txt**: Тут записываются логи всех неудачных действий в скрипте.

## Установка и запуск

1. Клонируем репозиторий:

    ```bash
    git clone https://github.com/Nomzegh/zetachain-automation.git
    ```

2. Устанавливаем нужные библиотеки:

    ```bash
    pip install requests
    pip install web3
    ```

3. Меняем, или оставляем значения в `config.py`.

4. Загружаем `keys.txt` приватными ключами с ZETA в Zetachain и BNB в BSC на балансе.

5. Запускаем:

    ```bash
    python main.py
    ```
6. Вписываем номер желаемой функции (1-10), ждем результата.



## Примечания
- Так как API от Zetahub обновляется немного медленно, клейм квестов / проверку профиля нужно запускать, подождав пару минут после отправки транзакций.

- Убедитесь, что на кошельках есть нужный баланс

- Обязательно настройте все значения в `config.py` под себя

## Затраты
Для выполнения круга транзакций, нам нужны монеты ZETA в Zetachain и BNB в Binance Smart chain. Все значения подсчитаны для **1 аккаунта** и на **1 неделю**.

1. **Enroll:**  ~0.001202 ZETA fee
2. **Send & Receive Zeta:** ~0.000212 ZETA fee
3. **Receive BNB in ZetaChain:** ~0.0000231 BNB fee при 1.1 gwei + пересылаемые BNB
4. **BNB Approve for LP:** ~0.000302 ZETA fee
5. **LP Any Core Pool:** ~0.001441 ZETA fee + BNB и ZETA которые депозитим в пул (в конфиге рабочие значения)
6. **Receive BTC & ETH:** ~0.006 ZETA (fee + min value)

#
- **Total BNB:** ~0.0000231 BNB ($0.0073) + желаемые BNB для депозита в пул.
- **Total ZETA:** ~0.009157 ZETA ($0,012) + желаемые ZETA для депозита в пул.

- Ко всему этому, нужно еще добавить две комиссии: за пересыл BNB в бск и ZETA в зете (за пересыл между мейном и мультиакком)
#

# Code by https://t.me/roccrypto


Solute To Russian Friends！Nice guys!
里面说明几点：
1. 由于我节点少，所以暂时封印了 proxies，各位需要可以仿照原项目加上
2. 比起俄国朋友的版本，加上了工作流，可以直接运行
3. pip install fake-useragent

# Update by https://github.com/tengda89757/zeta-fandou
# 在以上作者基础之上增加了异步重试
1. 在functions.py中的get_proxy函数注意要自己去购买一个代理，或者实现自己的代理，购买链接：https://app.nstproxy.com/register?i=OkMHd2
2. main.py的asyncio.Semaphore(20) 是代理池大小，可以自己修改，最好不要太高，失败率会显著增加
3. functions.py中的retry函数控制重试次数，可以根据自己的网络情况修改

## 注意点


```text
以下三个flow是每一个账号必须要做的，建议分开单独执行:
workflow = [1] // 认证账号
workflow = [2] // 查询授权是否成功, 未成功的将写入文件: enroll_verify_fail.txt
workflow = [5] // 单独授权 pool_tx


以下是完成任务:
workflow = [3, 4, 6, 7, 8, 9] // 执行获取xp任务
workflow = [10] // 单独领取奖励
workflow = [11] // 查询账号的xp奖励(可以不查)

每次执行成功的key会写入success_keys.txt中，下次执行会跳过。重复执行的时候根据需要看是否要清除掉。


```
