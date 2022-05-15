"""
MIT License

Copyright (c) 2021 ChrisDewa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class UnbError(Exception):
    """Base exception class for unbelipy."""
    pass

class ResponseError(UnbError):
    pass

class BadRequest(ResponseError):
    pass

class Unauthorized(ResponseError):
    pass

class Forbidden(ResponseError):
    pass

class NotFound(ResponseError):
    pass

class TooManyRequests(ResponseError):
    pass

class InternalServerError(ResponseError):
    pass

class UnknownError(UnbError):
    pass

API_ERRORS = {
    400: BadRequest,
    401: Unauthorized,
    403: Forbidden,
    429: TooManyRequests,
    500: InternalServerError
}
