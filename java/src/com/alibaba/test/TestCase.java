package com.alibaba.test;
import org.apache.commons.lang.StringUtils;

public class TestCase {

    public static void main(String[] args) {
        if (args.length != 6 || StringUtils.isEmpty(args[1])) {
            throw new IllegalArgumentException(args.toString());
        }

        System.out.println("TEST1");
        System.out.println("TEST2");

    }

}
