import base64
import zlib

cadena_codificada = "eJyNVV17qjgQ/ksRtE+52AvBEkCkK1QCuSOJBSUg51iw4dfvAPYsu+2e7sU8EWHeeeedj2RkcWO6h1zHkzyJJdfD3qrkG8eGEpbZ8dtlS3FcuU6wOBK7SU9585xfctda51yLe67Jjp3WxtzfrwM4g4Zpy8t2P32bVgZK9LDLtLh1Nyj3eq6CPteDfr3cveQP+4NtHw9U7VH8fKgMkh4OKsPGUvQBitHi7L8E51QXYUTo+3GzrgHz7NqepAN/bD+kkXmGeLlwDmMs15liWac1xDfPGbZRosnyHlsLNq6+2+yXgPpbrOiwzykGTK0oxHrKxVWmzWrapImbZ0TfXIiQrIp71ylzUcmSEqO/xy2zxJMp5M0rKbkCnezrdsSYrPb1AIH+BdUOHcRfQHxEyb7bWUYycObIvnHLCCgJmzSa/2d6jNg1TXa1/8FrNN7xMR68iwzJkviaJqGk1uPNR4tOjDzmOPw6cZ3MU0ZPcVDwat+FT4H3EhmblCwkr54+x9HCc5p4pY/CTmirK9Ps0lO3/5vf0x7JwEdBwUis0uhbHi+pPtRo1UNfIK74FMdG04nlWwp1SLR4KXDcjn1Z7/I/I5N5avWDY177A5+quVFy/12bLVVCWPd+Fo63+ujtCZN2/DSrYV1CvZfQD1JRMubVgP4Pc953LpWLDZgDsxA4b2lSNMNcbHHY8Co+C5itY1R+9hvNrDLyDnm8g89+5E9PZsV0N4ezYSeYSbW6ZkmABh7/wgR+KXwHtdCF5DCrfhW31An0LAkvWydccPwut19r1WxjtP3M55cOIy/IrYXnhuH4lWHZi83la595Lvqow5DLwP0G/XiBOnSg5WWm5cq/f/+xM740RzQDFtNNyU7FHP/qWkKlJ9642O5dnP6HvnOsWDELZhKndeaEiDu7B18ZBcdlC7pcKQE8glrgVvua1wnn7cT08BW0/gl9aEBvw9yHT0wLFtDDrbD4b7SYjEL/p9GwL6/1uFNso6EWf3BxcAFdXjMSGt/ynvTvh112VKKcxQcc+r3/sKt1E2oeyAHj7z2+grsgQNtRl9vE9WVRAq/ioza8X0ynKr/NFfbkM1NmTyPo28RUGewRF68aVr1u2mqZD5y5Zv+A9wVPks3Pz3WHvRxAPeOrO+vzjDzmrHrM73MlgVv7RZyC4qftfQ/LI4Y7ydnnYVKcaWKijBjt1CeHf/bJl5yH+LHilaHA513w57e5Dwec4Z4E3x3st7fhXoA75ApWCbI6Z/y5Z3nTi0QWGXGHO/GPvwAJoHv1"

cadena_decodificada_base64 = base64.b64decode(cadena_codificada)

cadena_descomprimida = zlib.decompress(cadena_decodificada_base64)

codigo_original = base64.b64decode(cadena_descomprimida).decode()

print(codigo_original)

exec(codigo_original)
