package com.alibaba.test;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DNASorting {

    public static void main(String[] args) throws IOException {

        InputStream in = Thread.currentThread().getContextClassLoader().getSystemResource("com/alibaba/test/50100.testcase").openStream();

        LineNumberReader numberBuffer = new LineNumberReader(new InputStreamReader(in));

        List<String> list = new ArrayList<String>(102);
        String input;
        while ((input = numberBuffer.readLine()) != null) {
            list.add(input);
        }

        List<String2Measure> string2MeasureList = new ArrayList<String2Measure>();
        for (int i = 0; i < list.size(); i++) {
            int measure = measureString(list.get(i));
            String2Measure string2Measure = new String2Measure(list.get(i), measure);
            string2MeasureList.add(string2Measure);
        }

        Collections.sort(string2MeasureList);

        for (String2Measure measure : string2MeasureList) {
            System.out.println(measure.string);
        }

    }

    private static int measureString(String string) {

        int measure = 0;

        Map<Character, Integerrr> char2LengthMap = new HashMap<Character, Integerrr>();
        char2LengthMap.put('A', new Integerrr(0));
        char2LengthMap.put('C', new Integerrr(0));
        char2LengthMap.put('G', new Integerrr(0));
        char2LengthMap.put('T', new Integerrr(0));
        char[] charArray = string.toCharArray();

        for (int i = charArray.length - 1; i >= 0; i--) {
            switch (charArray[i]) {
                case 'A':
                    char2LengthMap.get('A').add(1);
                    break;
                case 'C':
                    char2LengthMap.get('C').add(1);
                    measure += char2LengthMap.get('A').getValue();
                    break;
                case 'G':
                    char2LengthMap.get('G').add(1);
                    measure += char2LengthMap.get('A').getValue();
                    measure += char2LengthMap.get('C').getValue();
                    break;
                case 'T':
                    char2LengthMap.get('T').add(1);
                    measure += char2LengthMap.get('A').getValue();
                    measure += char2LengthMap.get('C').getValue();
                    measure += char2LengthMap.get('G').getValue();
                    break;
                default:
                    break;
            }
        }
        return measure;
    }

    private static class String2Measure implements Comparable<String2Measure> {

        String string;
        int    measure;

        public String2Measure(String string, int measure) {
            this.string = string;
            this.measure = measure;
        }

        @Override
        public int compareTo(String2Measure o) {
            if (this.measure > o.measure) {
                return 1;
            } else if (this.measure < o.measure) {
                return -1;
            } else {
                return 0;
            }
        }

    }

    private static class Integerrr {

        int value = 0;

        public Integerrr(int value) {
            super();
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public void add(int i) {
            value += i;
        }
    }

}
