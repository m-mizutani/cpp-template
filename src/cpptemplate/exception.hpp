#ifndef __CPPTEMPLATE_EXCEPTION_HPP
#define __CPPTEMPLATE_EXCEPTION_HPP

#include <exception>
#include <sstream>
#include <string>

namespace netdec {
namespace Exception {

// Exception::Error is base exception of cpptemplate.
// Exception classes of netdec should inherit Exception::Error
// if there is no special reason.

class Error : public std::exception {
 private:
  std::string errmsg_;
 public:
  explicit Error(const std::string &errmsg) : errmsg_(errmsg) {}
  virtual ~Error() throw() {}
  virtual const char* what() const throw() {
    return this->errmsg_.c_str();
  }
};

// ConfigError for invalid preparation.

class ConfigError : public Error {
 public:
  explicit ConfigError(const std::string &errmsg) : Error(errmsg) {}
};


}   // namespace Exception
}   // namespace netdec

#endif    // __CPPTEMPLATE_EXCEPTION_HPP
