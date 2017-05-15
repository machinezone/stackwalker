
BREAKPAD_SRCDIR := ../breakpad/src
BREAKPAD_OBJDIR := ../breakpad/src

BREAKPAD_LIBS := \
  $(BREAKPAD_OBJDIR)/libbreakpad.a \
  $(BREAKPAD_OBJDIR)/third_party/libdisasm/libdisasm.a \
  $(NULL)

JSON_DIR := jsoncpp-src-0.5.0
JSON_SRCDIR := $(JSON_DIR)/src/lib_json
JSON_INCLUDEDIR := $(JSON_DIR)/include

BINS := \
  stackwalker
  $(NULL)

all: $(BINS)

stackwalker_OBJS := \
  json_reader.o \
  json_value.o \
  json_writer.o \
  $(NULL)

VPATH += $(JSON_SRCDIR)

CXXFLAGS += \
  -I$(BREAKPAD_SRCDIR) \
  -I$(JSON_INCLUDEDIR) \
  -std=gnu++0x \
  -Wno-format \
  -Werror \
  -D__STDC_FORMAT_MACROS=1 \
  $(NULL)
LIBS := 

.SECONDEXPANSION:
$(BINS): %: %.cc $(BREAKPAD_LIBS) $$($$*_OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $< $(EXTRA_OBJS) $(BREAKPAD_LIBS) $($*_OBJS) $(LIBS)

clean:
	$(RM) $(BINS) *.o
